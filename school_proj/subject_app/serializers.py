from rest_framework import serializers
# Models
from .models import Subject
# Serializer
from student_app.serializers import StudentAllSerializer

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        # fields = ['subject_name', 'professor']
        fields = '__all__'
    
    def get_students(self, instance):
        students = instance.students.all()
        students_ser = StudentAllSerializer(students, many=True)
        return students_ser.data



