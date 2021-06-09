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
def qu(requests, it):
    questi = Question.objects.get(id=it)
    res = []
    answers = Answer.objects.all()
    for p in answers:
        if len(res) == 0:
            res.append(p)
        if len(res) >= 10:
            break
    for i in res:
        print(i.text)
        print(i.author)
    return render(requests, 'quest.html', {'question':questi, 'a':res})
def formdef(requests):
    if requests.method == "GET":
        form = AskForm()
    else:
        form = AskForm(requests.POST)
        if AskForm.clean(form):
            post = form.save()
            url = post.id
            return HttpResponseRedirect("/question/"+str(url))
    return render(requests, "forms.html", {"forms":form}) 
