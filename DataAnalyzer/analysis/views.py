import pandas as pd
import numpy as np
import io
import json
import plotly.express as px
import plotly.utils
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile

def upload_file(request):
    """
    Handles the file upload and data analysis. 
    If the request is POST, it processes the uploaded file and performs data analysis.
    If the form is valid, it reads the CSV, performs data analysis, saves the results in the database, 
    and renders the results page. Otherwise, it renders the upload form.
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the uploaded CSV file into a pandas DataFrame
            uploaded_file = request.FILES['file']
            df = pd.read_csv(io.BytesIO(uploaded_file.read()))

            # Perform basic data analysis
            data_summary, charts_data = analyze_data(df)

            # Save the uploaded file and analysis results to the database
            uploaded_file_instance = UploadedFile(
                file=uploaded_file,
                first_rows=data_summary['first_rows'],
                missing_values=pd.DataFrame(data_summary['missing_values'], columns=['Missing Values']).to_html()
            )
            uploaded_file_instance.save()

            # Render the results page with data analysis summary and Histogram Plots
            return render(request, 'analysis/result.html', {'data_summary': data_summary, 'charts_data': charts_data})
    else:
        # Render the upload form
        form = UploadFileForm()
    return render(request, 'analysis/index.html', {'form': form})

def analyze_data(df):
    """
    Performs basic data analysis on the provided DataFrame.
    - Displays the first 5 rows.
    - Calculates summary statistics for numerical columns.
    - Handles missing values by counting them.
    - Generates histograms for numerical columns (excluding the first column).
    
    Returns a summary of the data and generated charts.
    """
    # Display the first few rows of the DataFrame
    data_summary = {'first_rows': df.head().to_html()}

    # Calculate summary statistics for each numerical column
    for col in df.select_dtypes(include=[np.number]):
        data_summary[col] = df[col].describe().to_dict()

    # Handle missing values by counting them
    data_summary['missing_values'] = df.isnull().sum().to_dict()

    charts_data = {}
    numeric_columns = df.select_dtypes(include=[np.number]).columns

    if len(numeric_columns) > 1:
        # Drop the first column for plotting and generate histograms for the remaining columns
        for column in numeric_columns[1:]:
            cleaned_column = df[column].dropna()  # Handle missing values by dropping them
            fig = px.histogram(cleaned_column, x=cleaned_column, nbins=10, title=f'Histogram of {column}')
            charts_data[column] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return data_summary, charts_data
