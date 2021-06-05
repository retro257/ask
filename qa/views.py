from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Answer, Question 
def test(requests, *args, **kwargs):
    posts = Question.objects.new()
    return HttpResponse("OK")

