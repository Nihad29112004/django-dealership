from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Dealer, Review
from .forms import ReviewForm

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

class CustomLoginView(LoginView):
    template_name = 'main/login.html'

def logout_done(request):
    return render(request, 'main/logout_done.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def home(request):
    dealers = Dealer.objects.filter(status='active')
    return render(request, 'main/home.html', {'dealers': dealers})

def active_dealers(request):
    active_dealers_list = Dealer.objects.filter(status='active')
    return render(request, 'main/home.html', {'dealers': active_dealers_list})

def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = dealer.reviews.all()
    return render(request, 'main/dealer_detail.html', {'dealer': dealer, 'reviews': reviews})

@login_required
def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.dealer = dealer
            review.author = request.user.username
            review.save()
            return redirect('dealer_detail', dealer_id=dealer_id)
    else:
        form = ReviewForm()

    return render(request, 'main/add_review.html', {'form': form, 'dealer': dealer})
