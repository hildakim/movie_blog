from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import PhotoReview
from .forms import PhotoReviewForm

# Create your views here.
def home(request):
    allPost = PhotoReview.objects.all()
    return render(request, 'home2.html', {'allPost': allPost})

def detail(request, id):
    reviewPost = get_object_or_404(PhotoReview, pk = id)
    return render(request, 'detail2.html', {'reviewPost':reviewPost})
    
def new(request):
    form = PhotoReviewForm()
    return render(request, 'new2.html', {'form': form})

def create(request):
    form = PhotoReviewForm(request.POST, request.FILES)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.upload_date = timezone.now()
        new_review.save()
        return redirect('photoreview/detail', new_review.id)
    return redirect('photoreview')
    

def edit(request, id):
    edit_review = PhotoReview.objects.get(id = id)
    return render(request, 'edit2.html', {'review':edit_review})

def update(request, id):
    update_review = PhotoReview.objects.get(id = id)
    update_review.review_title = request.POST['review_title']
    update_review.movie = request.POST['movie']
    update_review.rating = request.POST['rating']
    update_review.upload_date = timezone.now()
    update_review.save()
    return redirect('photoreview/detail', update_review.id)

def delete(request, id):
    delete_review = PhotoReview.objects.get(id = id)
    delete_review.delete()
    return redirect('photoreview')
