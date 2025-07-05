from django.db import models
from django.contrib.auth.models import User
import random


class Quiz(models.Model):
  name = models.CharField(max_length=120)
  topic = models.CharField(max_length=120)
  number_of_questions = models.IntegerField()
  time = models.IntegerField(help_text="time in second")
  required_score_to_pass = models.IntegerField()
 

  def __str__(self):
    return f'{self.name} - {self.topic}' 
     
  def get_questions(self):
        questions = list(self.question_set.all())
        if len(questions) < self.number_of_questions:
            return questions
        selected_questions = random.sample(questions, self.number_of_questions)
        return sorted(selected_questions, key=lambda x: x.id)  # Urutkan berdasarkan ID
  
  class Meta:
    verbose_name_plural = "Quizzes"
  

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  option_a = models.CharField(max_length=100)
  option_b = models.CharField(max_length=100)
  option_c = models.CharField(max_length=100)
  correct_answer = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.title} = {self.correct_answer}'

  

class Result(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.user.username)
