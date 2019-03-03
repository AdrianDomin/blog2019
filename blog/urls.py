from django.urls import path
from . import views

urlpatterns = [
path('', views.post_list, name ='post_list'),
path('<int:slug>/', views.post_detail, name='post_detail'),
path('<int:publish_day>/', views.post_detail, name='post_detail'),
path('<int:publish_year>/', views.post_detail, name='post_detail'),
path('<int:publish_month>/', views.post_detail, name='post_detail')
]
