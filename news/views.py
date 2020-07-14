from django.shortcuts import render,redirect
from news.models import News, Slider, trending, read
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponseRedirect

def thesocialbugg(request):
    news = Slider.objects.all()
    news_tp = read.objects.all()[0:3]
    news_td = trending.objects.all()[0:3]
    return render(request, 'main.html', {'news_td':news_td , 'news_tp':news_tp , 'news':news })

def fullwidth(request,slug):
    news = News.objects.get(slug__iexact = slug)
    related = News.objects.filter(category = news.category)[0:2]
    recent = News.objects.all().order_by('-created')[0:5]
    return render(request, 'fullwidth.html', {'news':news,'recent':recent,'related':related})

def blog(request,category):
    news = News.objects.filter(category=category)
    recent = News.objects.all().order_by('-created')[0:5]
    paginator = Paginator(news,4)
    page = request.GET.get('page')
    news = paginator.get_page(page) 
    return render(request, 'blog.html', {'news':news,'recent':recent})

def terms(request):
    recent = News.objects.all().order_by('-created')[0:5]
    return render(request, 'terms.html', {'recent':recent})

def privacy(request):
    recent = News.objects.all().order_by('-created')[0:5]
    return render(request, 'privacy.html', {'recent':recent})

def search(request):
    recent = News.objects.all().order_by('-created')[0:5]
    if request.GET.get('s'): # this will be GET now      
        news_title =  request.GET.get('s') # do some research what it does       
        try:
            status = News.objects.filter(title__icontains=news_title) # filter returns a list so you might consider skip except part
        except:
            return redirect(request,"notfound.html",{'recent':recent})
    else:
        return render(request, 'search.html', {'recent':recent})

    if status:
        paginator = Paginator(status,4)
        page = request.GET.get('page')
        status = paginator.get_page(page) 
        return render(request,'search.html',{'news':status,'recent':recent})
    else:
        return HttpResponseRedirect("/notfound/")
    

def notfound(request):
    recent = News.objects.all().order_by('-created')[0:5]
    return render(request,'notfound.html',{'recent':recent})
