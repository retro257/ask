from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Answer, Question
from django.shortcuts import render 
def test(requests, *args, **kwargs):
    posts = Question.objects.new()
    limit = 10
    page = requests.GET.get("page", 1)
    paginator = Paginator(posts, limit)
    page = paginator.page(page)
    return render(requests, 'main.html', {paginator:paginator})

