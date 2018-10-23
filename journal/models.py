from django.db import models

# Create your models here.
class Entries(models.Model):
    user_ID = models.IntegerField(default=0)
    entry_text = models.CharField(max_length=4000)
    submission_date = models.DateTimeField('date published')
    anger = models.DecimalField(decimal_places=6,max_digits=7)
    disgust = models.DecimalField(decimal_places=6,max_digits=7)
    fear = models.DecimalField(decimal_places=6,max_digits=7)
    joy = models.DecimalField(decimal_places=6,max_digits=7)
    sadness = models.DecimalField(decimal_places=6,max_digits=7)
    analytical = models.DecimalField(decimal_places=6,max_digits=7)
    confident = models.DecimalField(decimal_places=6,max_digits=7)
    tentative = models.DecimalField(decimal_places=6,max_digits=7)
    openness = models.DecimalField(decimal_places=6,max_digits=7)
    conscientiousness = models.DecimalField(decimal_places=6,max_digits=7)
    extraversion = models.DecimalField(decimal_places=6,max_digits=7)
    agreeableness = models.DecimalField(decimal_places=6,max_digits=7)
    emotional_range = models.DecimalField(decimal_places=6,max_digits=7)
    def __str__(self):
        return self.entry_text
    def get_absolute_url(self):
        return reverse('entries-detail', kwargs={'pk': self.pk})
