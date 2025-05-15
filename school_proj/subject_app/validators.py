from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    subject_pattern = re.compile(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$')
    
    if not subject_pattern.match(value):
        raise ValidationError("Subject must be in title case format.")


def validate_professor_format(value):
    professor_pattern = re.compile(r'^Professor\s[A-Z][a-z]+$')

    if not professor_pattern.match(value):
        raise ValidationError('Professor name must be in the format "Professor Adam".')
