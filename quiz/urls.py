from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('scores/', views.scores_quiz, name='scores_quiz'),
    path('scores_all/', views.result_quiz_all, name='result_quiz_all'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('<int:pk>/take/', views.quiz_take, name='quiz_take'),
    path('<int:pk>/submit/', views.quiz_submit, name='quiz_submit'),
    path('quiz/<int:pk>/result/', views.quiz_result, name='quiz_result'),
]
