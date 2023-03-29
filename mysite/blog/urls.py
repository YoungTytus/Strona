from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('about/', AboutView, name='about'),
    path('posts/', PostsView.as_view(), name='posts'),
]
