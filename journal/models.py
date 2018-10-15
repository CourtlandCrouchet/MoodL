from django.db import models

# Create your models here.
class Entries(models.Model):
    user_ID = models.IntegerField(default=0)
    entry_text = models.CharField(max_length=4000)
    submission_date = models.DateTimeField('date written')
    anger = models.IntegerField(default=0)
    disgust = models.IntegerField(default=0)
    fear = models.IntegerField(default=0)
    joy = models.IntegerField(default=0)
    sadness = models.IntegerField(default=0)
    analytical = models.IntegerField(default=0)
    confident = models.IntegerField(default=0)
    tentative = models.IntegerField(default=0)
    openness = models.IntegerField(default=0)
    conscientiousness = models.IntegerField(default=0)
    extraversion = models.IntegerField(default=0)
    agreeableness = models.IntegerField(default=0)
    emotional_range = models.IntegerField(default=0)
