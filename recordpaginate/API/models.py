from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class cases(models.Model):
    objects = None
    id = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=99)
    reference = models.CharField(max_length=999)
    description = models.CharField(max_length=9999)
    extra = models.CharField(max_length=99)


class labs(models.Model):
    objects = None
    id = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    province = models.CharField(max_length=99)
    name = models.CharField(max_length=99)
    city = models.CharField(max_length=99)
    sector = models.CharField(max_length=99)
    reference = models.CharField(max_length=99)

class quarantine(models.Model):

    id = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    province = models.CharField(max_length=99)
    name = models.CharField(max_length=99)
    beds = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    reference = models.CharField(max_length=99)

class sqliteseq(models.Model):
    name = models.CharField(max_length=999)
    seq = models.CharField(max_length=999)

class summery(models.Model):
    id = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    total_test = models.CharField(max_length=9999)
    total_cases = models.CharField(max_length=9999)
    total_recovered = models.CharField(max_length=9999)
    total_deaths = models.CharField(max_length=9999)
    total_critical = models.CharField(max_length=9999)
    last_test = models.CharField(max_length=9999)
    last_cases = models.CharField(max_length=9999)
    last_recovered = models.CharField(max_length=9999)
    last_deaths = models.CharField(max_length=9999)
    last_critical = models.CharField(max_length=9999)
    reference = models.CharField(max_length=9999)


class vaccine(models.Model):
    id = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], primary_key=True)
    datetime = models.CharField(max_length=999)
    total_fully = models.CharField(max_length=999)
    total_partially = models.CharField(max_length=999)
    total_doses = models.CharField(max_length=999)
    last_fully = models.CharField(max_length=999)
    last_partially = models.CharField(max_length=999)
    last_doses = models.CharField(max_length=999)
    reference = models.CharField(max_length=999)

