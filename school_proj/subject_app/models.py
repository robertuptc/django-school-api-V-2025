from django.db import models
from .validators import validate_subject_format, validate_professor_format

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_subject_format]
    )
    professor = models.CharField(
        max_length=255, null=False, blank=False, default='Professor.Cahan', validators=[validate_professor_format]
    )

    def __str__(self):
        return f"{self.subject_name} - {self.professor} {self.students.count()}"

    def add_a_student(self, stud_id):
        if self.students.count() < 31:
            self.students.add(stud_id)
        else:
            raise Exception("This subject is full!")

    def drop_a_student(self, stud_id):
        if self.students.count() > 0:
            self.students.remove()
        else:
            raise Exception("This subject is empty!")