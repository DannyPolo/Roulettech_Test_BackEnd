from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length=30)
    lastName = models.TextField(max_length=30)
    email = models.EmailField(max_length=254)
    age = models.PositiveIntegerField()
    grade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name, self.lastName, self.email, self.age, self.grade