from django.db import models

# Create your models here.
class Class(models.Model):
    name=models.IntegerField()

    def __str__(self):
        return str(self.name)

    

class Division(models.Model):
    name=models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField(unique=True)
    class_name=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='class_details')
    division=models.ForeignKey(Division,on_delete=models.CASCADE,related_name='division_details')

    def __str__(self):
        return self.name

class Marks(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    math_mark=models.IntegerField()
    english_mark=models.IntegerField()
    malayalam_mark=models.IntegerField()

