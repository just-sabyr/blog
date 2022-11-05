from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Posts page.
    path('posts', views.posts, name='posts'),
    # Detail for a single post.
    path('post/<int:post_id>/', views.post, name='post'),
    # All comments to a post.
    path('posts/<int:post_id>/comments', views.comments, name='comments'),
    # Page for adding a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for adding a new comment.
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),
]
