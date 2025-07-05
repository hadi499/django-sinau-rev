from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_view, name='posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]
