from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.
def home(request):
    allPost = Blog.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

def detail(request, id):
    reviewPost = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'reviewPost':reviewPost})
    
def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.upload_date = timezone.now()
        new_review.save()
        return redirect('detail', new_review.id)
    return redirect('home')
    # new_review = Blog()
    # new_review.review_title = request.POST['review_title']
    # new_review.nickname = request.POST['review_writer']
    # new_review.movie = request.POST['movie']
    # new_review.review_body = request.POST['review_body']
    # new_review.image = request.FILES['image']
    # new_review.upload_date = timezone.now()
    # new_review.save()
    

def edit(request, id):
    edit_review = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'review':edit_review})

def update(request, id):
    update_review = Blog.objects.get(id = id)
    update_review.review_title = request.POST['review_title']
    update_review.nickname = request.POST['review_writer']
    update_review.movie = request.POST['movie']
    update_review.review_body = request.POST['review_body']
    update_review.upload_date = timezone.now()
    update_review.save()
    return redirect('detail', update_review.id)

def delete(request, id):
    delete_review = Blog.objects.get(id = id)
    delete_review.delete()
    return redirect('home')
