from django.db import models 
from django.contrib.auth.models import User 
from django.http import HttpResponseNotFound 
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')
    def obj(id):
#        try:
        question = Question.objects.get(id=id) 
#        finally:
#            return HttpResponseNotFound  
        answers = Answer.objects.filter(question=question)
        res = []
        limit = 10
        for i in answers:
            if len(res) == 0:
                res.append(i)
            if len(res) >= limit:
                break
        return res 
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})
    def __unicode__(self):
        return self.title 
class Answer(models.Model):
    objects = QuestionManager()
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)
