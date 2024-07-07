from django.urls import path
from .views import home_view,contact_view,blog_view,BlogDetailView #blog_detail_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('contact/',contact_view,name='contact-page'),
    path('blogs/',blog_view,name='blog-page'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(),name='blog-detail-page')
]
