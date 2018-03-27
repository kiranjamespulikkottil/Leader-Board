from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Score(models.Model):
    class Meta:
            ordering = ['-score']

    scoreadmin = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,primary_key=True)
    score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('score_detail', args=[str(self.name)])


    def __str__(self):
        return self.name
