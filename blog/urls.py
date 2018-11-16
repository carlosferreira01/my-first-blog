from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_list/about', views.about, name='about'),
    path('post_list/contact', views.contact, name='contact'),
]
