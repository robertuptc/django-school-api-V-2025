from django.db import models
from django.core import validators as v
from .validators import (
    validate_combination_format,
    validate_name_format,
    validate_school_email,
)

# Models
from subject_app.models import Subject

# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name_format]
    )
    student_email = models.EmailField(
        null=False, blank=False, unique=True, validators=[validate_school_email]
    )
    personal_email = models.EmailField(null=False, blank=False, unique=True)
    locker_number = models.IntegerField(
        default=110,
        null=False,
        blank=False,
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        default="12-12-12",
        null=False,
        blank=False,
        max_length=255,
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, related_name="students")

    def remove_subject(self, class_id):
        if self.subjects.count() > 0:
        # if len(self.subjects.all()) > 0:
            self.subjects.remove(class_id)
        else:
            raise Exception("This students class schedule is empty!")
    
    def add_subject(self, class_id):
        if self.subjects.count() < 8:
            self.subjects.add(class_id)
        else:
            raise Exception("This students class schedule is full!")


