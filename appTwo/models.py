from django.db import models
from datetime import datetime

# Create your models here.
from django.utils.timezone import now

from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)


class EspTest(models.Model):
    isTremor = models.CharField(max_length=128, default="NULL")
    isFall = models.CharField(max_length=128, default="NULL")
    latValue = models.CharField(max_length=128, default="NULL")
    longValue = models.CharField(max_length=128, default="NULL")
    safeDist = models.CharField(max_length=128, default="NULL")
    isSafe = models.CharField(max_length=128, default="NULL")
    bpm = models.CharField(max_length=128, default="NULL")


class AccModel(models.Model):
    isTremor = models.CharField(max_length=128, default="NULL")
    isFall = models.CharField(max_length=128, default="NULL")
    isPressed = models.CharField(max_length=128, default="NULL")
    updated = models.DateTimeField(auto_now=True)


class GpsModel(models.Model):
    latValue = models.CharField(max_length=128, default="NULL")
    longValue = models.CharField(max_length=128, default="NULL")
    safeDist = models.CharField(max_length=128, default="NULL")
    isSafe = models.CharField(max_length=128, default="NULL")
    bpm = models.CharField(max_length=128, default="NULL")
    updated = models.DateTimeField(auto_now=True)
