# from django.test import TestCase
# from django.core.exceptions import ValidationError
# # Models
# from .models import Grade

# Create your tests here.
# class Grade_test(TestCase):
    # def test_01_create_grade_with_incorrect_grade_field(self):
    #     new_grade = Grade(grade=101)

    #     try:
    #         new_grade.full_clean()
    #     except ValidationError as e:
    #         self.assertIn('Ensure this value is less than or equal to 100.0.', str(e))

    # def test_02_create_grade_with_incorrect_grade_field_decimals(self):
    #     new_grade = Grade(grade=101.11)

    #     try:
    #         new_grade.full_clean()
    #     except ValidationError as e:
    #         self.assertIn('Ensure this value is less than or equal to 100.0.', str(e))