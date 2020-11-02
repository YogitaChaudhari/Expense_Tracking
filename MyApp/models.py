from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=30)
    incomeDate=models.DateField()
    incomeDescription=models.TextField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=30)
    expenseDate=models.DateField()
    expenseDescription=models.TextField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
