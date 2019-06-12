#####在这里写上要开发的内容，比如：
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
	return HttpResponse('index')

def login(request):
	return redirect('/index')


