from django.shortcuts import render
from  . import models
# from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse('HELLO WORLD')
	articles = models.Article.objects.all()
	return render(request,'index.html',{'articles':articles})
	# return render(request,'index.html',{'hello':'hello today!!!'})

def article_page(request,article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request,'article_page.html',{'article':article})

