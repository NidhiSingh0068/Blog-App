from . import views
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('search', views.search, name="search"),
   
  
]
    
