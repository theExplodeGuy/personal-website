from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('blog/<slug:slug>/', views.blog_detail, name='post_detail'),
    path('home/<slug:slug>/', views.HomeDetails.as_view(), name='qualification_detail'),
    path('projects/', views.project_index, name="project_index"),
    path('projects/<int:pk>/', views.project_detail, name="project_detail"),
]
