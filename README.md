# Django-Based-Data-Analyzer
## Overview                
Data Analyzer is a Django-based web application that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on the web interface. The project covers basic data analysis tasks such as displaying the first few rows of the data, calculating summary statistics, identifying and handling missing values, and generating basic plots using matplotlib, seaborn & Plotly.

## Features
- File Upload: Users can upload CSV files via a Django web form.
- Data Processing: The application uses pandas to read the uploaded CSV files and perform basic data analysis.
- Data Visualization: The application generates histograms for numerical columns and displays them on the web page.
- User Interface: The application uses Django templates to create a simple and user-friendly interface for displaying data analysis results and visualizations.
## Requirements
- Python 3.12
- Django 5
- pandas
- numpy
- matplotlib or seaborn
- plotly
## Setup Instructions
### 1. Clone the Repository
    git clone https://github.com/RushikeshBihade/Django_Bsased_DataAnalyzer_WebApp.git
    cd data-analyzer
### 2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `nvenv\Scripts\activate`
### 3. Install the Dependencies
    pip install -r requirements.txt
### 4. Set Up the Database
    python manage.py migrate
### 5. Run the Development Server
    python manage.py runserver
### 6. Access the Application
Open your web browser and navigate to `http://127.0.0.1:8000/.`

## Project Structure
- dataAanalyzer/: The main Django project directory.
- analysis/: The Django app handling file uploads and data analysis.
- Datasets/: Contains Sample Datasets(iris, Healthcare).
- migrations/: Database migrations.
- static/analysis/: Static files (CSS, images, etc.).
- templates/analysis/: HTML templates.
- admin.py: Django admin configuration.
- apps.py: App configuration.
- forms.py: Form definitions.
- models.py: Data models.
- tests.py: Test cases.
- urls.py: URL routing.
- views.py: View functions.
- manage.py: Django's command-line utility.
## Usage
### Uploading a CSV File
Navigate to the home page.
Use the file input form to select a CSV file (e.g., iris.csv or healthcare.csv).
Click the "Generate Report" button to upload the file and perform data analysis.
### Viewing Data Analysis Results
After uploading a CSV file, the application will display:

- The first few rows of the data.
- Summary statistics (mean, median, standard deviation) for numerical columns.
- Missing values count for each column.
- Histograms for numerical columns.
## Sample Datasets
- Iris Dataset: A dataset containing measurements of iris flowers.
- Healthcare Dataset: A dataset containing healthcare-related data.
Both sample datasets are included in the data/ directory for testing purposes.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the Private License. See the LICENSE file for details.

## Acknowledgements
This project uses the following libraries and frameworks:

- Django
- pandas
- numpy
- JSON
- io
- matplotlib / seaborn
- plotly
## Contact
For any questions or feedback, please contact rushikeshbihade09@gmail.com.