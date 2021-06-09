from django.db import models 
from django.contrib.auth.models import User 
from django.http import HttpResponseNotFound
from django.urls import reverse 
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating') 
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    def get_absolute_url(self):
        return reverse('single-question-view', kwargs={'qa_id': self.id})
    def __unicode__(self):
        return self.title 
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.DO_NOTHING)
