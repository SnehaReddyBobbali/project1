from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_enrollment = models.DateField()

    def __str__(self):
        return self.name
