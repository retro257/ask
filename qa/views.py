from django.http import HttpResponse, HttpResponseRedirect 
from django.core.paginator import Paginator 
from qa.models import Answer, Question, QuestionManager 
from django.shortcuts import render
from qa.forms import AskForm, AnswerForm, Login, log
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
import django.contrib.sessions  
def test(requests, *args, **kwargs):
    posts = Question.objects.order_by('-id')
    limit = requests.GET.get('limit', 10)
    page = requests.GET.get("page", 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(requests, 'main.html', {'questions': page.object_list,'paginator': paginator, 'page': page,})
def qu(requests, qa_id):
    question = Question.objects.get(id=qa_id)
    answers = Answer.objects.filter(question=question)
    if requests.method == "GET":
        form = AnswerForm()
    else:
        form = AnswerForm(requests.POST)
        post = Answer(form.cleaned_data)
        post.save()
        return HttpResponseRedirect("/question/"+str(qa_id)+"/")
    return render(requests, "quest.html", {"question":question, "a":answers, "form":form})
def formdef(requests):
    if requests.method == "GET":
        form = AskForm()
    else:
        form = AskForm(requests.POST)
        if AskForm.clean(form):
            post = form.save()
            url = Question.objects.get(author_id = 1)
            print(url.id)
            return HttpResponseRedirect("/question/"+str(url.id)+"/")
    return render(requests, "forms.html", {"forms":form}) 
def signup(requests): 
    if requests.method == "GET":
        form = Login()
    else:
        form = Login(requests.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            username = requests.POST['username']
            password = requests.POST['password'] 
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(requests,user)
            requests.session['sessionid'] = get_random_string(32)
            return HttpResponseRedirect("/") 
    return render(requests, "signup.html", {"form":form}) 
def view_login(requests):
    if requests.method == "GET":
        form = log()
    else:
        form = log(requests.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                user = User.objects.get(username=form.cleaned_data['username'], password=salt_and_hash(form.cleaned_data['password']))
                requests.session['sessionid'] = get_random_string(32) 
                return HttpResponseRedirect("/")
            except User.DoesNotExist:
                return HttpResponse("your password/login not found")
    return render(requests, "login.html", {"form":form}) 
