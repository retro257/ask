from django.http import HttpResponse 
def test(requests, *args, **kwargs):
    return HttpResponse("OK")
