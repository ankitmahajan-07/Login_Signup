from django.db import models

# Create your models here.
class signup(models.Model):
    Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField()
    Dob = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)

    def __str__(self):
        return self.Username


