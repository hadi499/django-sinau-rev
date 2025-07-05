import json
from quiz.models import Question 
with open('question2.json') as f:
  question_json = json.load(f)

for question in question_json:
  question = Question(quiz_id=question['quiz_id'], title=question['title'], option_a=question['option_a'], option_b=question['option_b'], option_c=question['option_c'],correct_answer=question['correct_answer'])
  question.save()
  