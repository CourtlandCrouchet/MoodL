from django.db import models
from MoodL import watson_request
import datetime
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
    def analyze(self):
        if self.entry_text != "":
            self.mood_dict = watson_request.get_tone(self.entry_text)
            self.anger = self.mood_dict["anger"]
            self.disgust = self.mood_dict["disgust"]
            self.fear = self.mood_dict["fear"]
            self.joy = self.mood_dict["joy"]
            self.sadness = self.mood_dict["sadness"]
            self.analytical = self.mood_dict["analytical"]
            self.confident = self.mood_dict["confident"]
            self.tentative = self.mood_dict["tentative"]
            self.openness = self.mood_dict["openness"]
            self.conscientiousness = self.mood_dict["conscientiousness"]
            self.extraversion = self.mood_dict["extraversion"]
            self.agreeableness = self.mood_dict["agreeableness"]
            self.emotional_range = self.mood_dict["emotional range"]
        return self
    @classmethod
    def create(cls, text):
        entry = cls(entry_text=text)
        entry.submission_date = datetime.datetime.now()
        entry.analyze()
        entry.save()
        return entry
