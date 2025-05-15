# Django
from django.db import models
from django.core.validators import MaxValueValidator
# Models
from subject_app.models import Subject
from student_app.models import Student

# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        null=False, 
        blank=False, 
        default=100, 
        max_digits=5, 
        decimal_places=2, 
        validators=[MaxValueValidator(100.00)]
        )
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')