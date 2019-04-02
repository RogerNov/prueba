from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datos publicados')

    def _str_(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def _str_(self):
        return self.choice_text