from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserModel(AbstractUser):
    def __str__(self):
        return self.username

class ProfileModel(models.Model):
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    gender = models.CharField(choices=GENDER, null=True)
    age = models.IntegerField(null=True)
    height = models.FloatField(help_text='In CM',null=True)
    weight = models.FloatField(help_text='In KG', null=True)
    bmr = models.FloatField(null=True)

    @property
    def bmr(self):
        if not all([self.gender, self.weight, self.height, self.age]):
            return 0.0
        if self.gender == 'Male':
            return 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        elif self.gender == 'Female':
            return 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)

        return 0.0

    def __str__(self):
        return self.firstName
    
class CaloryConsumptionModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200,null=True)
    calory = models.FloatField(null=True)

    def __str__(self):
        return self.itemName
