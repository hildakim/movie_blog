from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    allPost = Blog.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

def detail(request, id):
    diaryPost = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'diaryPost':diaryPost})
    
def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Blog()
    new_diary.diary_title = request.POST['diary_title']
    new_diary.nickname = request.POST['diary_writer']
    new_diary.diary_body = request.POST['diary_body']
    new_diary.upload_date = timezone.now()
    new_diary.save()
    return redirect('detail', new_diary.id)

def edit(request, id):
    edit_diary = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'diary':edit_diary})

def update(request, id):
    update_diary = Blog.objects.get(id = id)
    update_diary.diary_title = request.POST['diary_title']
    update_diary.nickname = request.POST['diary_writer']
    update_diary.diary_body = request.POST['diary_body']
    update_diary.upload_date = timezone.now()
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_diary = Blog.objects.get(id = id)
    delete_diary.delete()
    return redirect('home')
