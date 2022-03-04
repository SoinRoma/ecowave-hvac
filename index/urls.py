
from django.contrib import admin
from django.urls import path
from . import views, api_views
app_name='index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/detail/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('create_feedback/', api_views.CreateFeedbackRequestView.as_view(), name='feedback_create'),
]
