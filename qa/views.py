from django.http import HttpResponse 
from django.core.paginator import Paginator 
from qa.models import Answer, Question, QuestionManager 
from django.shortcuts import render 
def test(requests, *args, **kwargs):
    posts = Question.objects.order_by('-id')
    limit = requests.GET.get('limit', 10)
    page = requests.GET.get("page", 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(requests, 'main.html', {'questions': page.object_list,'paginator': paginator, 'page': page,})
def qu(requests, it):
    questi = Question.objects.get(id=it)
    print(it)
    answers = Answer.objects.filter(question_id=questi.id)
    for i in answers:
        print(i.text)
        print(i.author)
    return render(requests, 'quest.html', {'question':questi, 'answers':answers})
