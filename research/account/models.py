from django.db import models
from django import forms

class research(models.Model):
    STATUS_CHOICES = (
        ('E', 'Editing'),
        ('A', 'Available'),
        ('X', 'Expired'),
    )

    PUBLISH_CHOICES = (
    	('T', 'Publish'),
        ('F', 'Not publish now'),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_at = models.DateField()
    finish_at = models.DateField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    count = models.IntegerField(default=0)
    publish = models.CharField(max_length=4, choices=PUBLISH_CHOICES)

    class Meta:
        app_label = "account"

class multiple_choice(models.Model):
    question = models.CharField(max_length=50)
    alt_1 = models.CharField(max_length=20)
    alt_2 = models.CharField(max_length=20)
    alt_3 = models.CharField(max_length=20)

    class Meta:
        app_label = "account"

class dissertative(models.Model):
    question = forms.CharField(max_length=50)
    answer = forms.CharField(max_length=1000, widget=forms.Textarea)
    class Meta:
        app_label = "account"
