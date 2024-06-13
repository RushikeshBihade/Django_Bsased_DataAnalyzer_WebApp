from django import forms

class UploadFileForm(forms.Form):
    """
    Form for uploading a CSV file.
    """
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'fileclass'}))