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
        post = Question(**self.cleaned_data)
        post.save()
        return post
class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.ChoiceField()
    def clean(form):
        if form.is_valid():
            return True
        else:
            return False
    def save(self):
        post = Answer(**self.cleaned_data)
        post.save()
        return post
