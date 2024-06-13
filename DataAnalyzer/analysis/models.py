from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    """
    Model to store the uploaded CSV file and its corresponding data analysis results.
    """
    # Field to store the uploaded file
    file = models.FileField(upload_to='uploads/')
    
    # Field to store the the data as HTML
    first_rows = models.TextField()
    summary_stats = models.TextField()
    missing_values = models.TextField()

    def __str__(self):
        """
        Returns the name of the uploaded file.
        """
        return self.file.name