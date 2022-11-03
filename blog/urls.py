from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("post_add/", views.PostCreateView.as_view(), name="blog_views_post_add"),
]
