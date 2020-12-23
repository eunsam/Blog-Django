from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Blog

def write(request):
    return render(request, 'blog/write.html')

def wrCon(request):
    title = request.POST['title']
    detail = request.POST['detail']

    qs = Blog(b_title=title, b_detail=detail)
    qs.save()

    return HttpResponseRedirect(reverse('blog:main'))

def main(request):
    qs = Blog.objects.all()
    context = {'blog_list':qs}
    return render(request, 'blog/main.html', context)

def viewDet(request, title):
    qs = Blog.objects.get(b_title=title)
    context = {'blog_detail':qs}
    return render(request, 'blog/view.html', context)

def modDet(request, title):
    return render(request, 'blog/modify.html')

def modCon(request):
    title = request.POST['title']
    detail = request.POST['detail']

    b_qs = Blog.objects.get(title=b_title)
    b_qs.b_title = title
    b_qs.b_detail = detail
    b_qs = Blog(b_title=title, b_detail=detail)
    b_qs.save()

    return HttpResponseRedirect(reverse('blog:viewDet'))

def delPost(request, title):
    qs = Blog.objects.get(b_title=title)
    qs.delete()

    return HttpResponseRedirect(reverse('blog:main'))
