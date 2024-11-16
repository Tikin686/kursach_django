from blog.views import BlogListView, BlogUpdateView, BlogDeleteView, BlogDetailView, BlogCreateView
from django.urls import path
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/detail/<slug:slug>", BlogDetailView.as_view(), name="blog_detail_slug"),
]
