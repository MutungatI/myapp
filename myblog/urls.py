from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('myblog_home/',PostListView.as_view(),name='post-list'),
    path('myblog/new/',PostCreateView.as_view(),name='post-create'),
    path('myblog/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('myblog/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('myblog/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]