from django.db import models

class Textbook(models.Model):
    # Condition choices - this ensures data consistency
    CONDITION_CHOICES = [
        ('new', 'Like New'),
        ('written', 'Written In'),
        ('old', 'Old'),
        ('fair', 'Fair'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=50, blank=True, null=True)  # Optional field
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    course_code = models.CharField(max_length=10)  # e.g., "COMP346"
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.course_code}"
