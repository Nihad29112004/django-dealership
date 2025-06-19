from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='logout_done'), name='logout'),
    path('logout/done/', views.logout_done, name='logout_done'),
    path('register/', views.register, name='register'),
    path('dealers/active/', views.active_dealers, name='active_dealers'),
    path('dealer/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),


]
