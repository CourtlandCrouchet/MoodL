from django.db import models
from MoodL import watson_request
import datetime
# Main Entry model, contains creating user's ID, date of
# submission, and all analyzed fields from IBM Tone Analyzer
class Entries(models.Model):
    user_ID = models.CharField(max_length = 100)
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
    def __str__(self): #Stringify method returns entry text
        return self.entry_text
    def get_absolute_url(self):
        return reverse('entries-detail', kwargs={'pk': self.pk})
    def analyze(self):
        if self.entry_text != "": #if entry_text is not empty
            #use IBM's Watson Tone Analyzer to analyze the entry text
            self.mood_dict = watson_request.get_tone(self.entry_text)
            #populate database with entry's analytics
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
    #helper method for creating a new Entry object
    #text = entry text
    #user_id = user ID of the writer
    @classmethod
    def create(cls, text, user_id):
        entry = cls(entry_text=text) #Set Entry's entry_text
        entry.submission_date = datetime.datetime.now() #submission date = now
        entry.user_ID = user_id #Save submitter's user ID
        entry.analyze() #analyze entry
        entry.save() #store Entry object to database
        return entry
