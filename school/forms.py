from django.forms import ModelForm
from .models import Student,Class,Division,Marks

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'