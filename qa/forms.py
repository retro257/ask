from django import forms
from qa.models import Question, Answer
class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    def clean(form):
        if form.is_valid():
            return True
        else:
            return False
    def save(self): 
        question = Question(self.cleaned_data) 
        question.author_id = 1 
        question.save() 
        return question        
    def clean(form):
        if form.is_valid(): 
            return True
        else:
            return False
    def add_author(author):
        quest = Question.objects.get()
class AnswerForm(forms.Form): 
    text = forms.CharField() 
    question = forms.ChoiceField() 
    def save(self):
        post = Answer(self.cleaned_data)
        post.save()
        return post
class Login(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()    
    def save(self, ok):
        post = self.cleaned_data[ok]
        return post 
class log(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
