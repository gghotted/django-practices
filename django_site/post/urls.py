from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', views.PostDetailUpdateDestroyAPIViewlAPIView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view()),
]
