from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey('Director', on_delete=models.DO_NOTHING, null=True, blank=True)
    accounts = models.ManyToManyField('Account')


class Client(models.Model):
    name = models.CharField(max_length=100)


class Account(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
