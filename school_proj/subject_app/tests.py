# from django.test import TestCase
# from django.core.exceptions import ValidationError
# # Model
# from .models import Subject

# # Create your tests here.


# class Subject_test(TestCase):
    # def test_01_create_subject_with_incorrect_subject_name(self):
    #     new_subject = Subject(subject_name="english", professor="Professor Robert")

    #     try:
    #         new_subject.full_clean()
    #     except ValidationError as e:
    #         self.assertIn('Subject must be in title case format.', str(e))

    # def test_02_create_subject_with_incorrect_professor(self):
    #     new_subject = Subject(subject_name="English", professor="Robert")

    #     try:
    #         new_subject.full_clean()
    #     except ValidationError as e:
    #         self.assertIn('Professor name must be in the format "Professor Adam".', str(e))
