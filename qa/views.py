from django.http import HttpResponse, HttpResponseRedirect 
from django.core.paginator import Paginator 
from qa.models import Answer, Question, QuestionManager 
from django.shortcuts import render
from qa.forms import AskForm, AnswerForm 
def test(requests, *args, **kwargs):
    posts = Question.objects.order_by('-id')
    limit = requests.GET.get('limit', 10)
    page = requests.GET.get("page", 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(requests, 'main.html', {'questions': page.object_list,'paginator': paginator, 'page': page,})
def qu(requests, qa_id):
    return HttpResponse('200')
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
