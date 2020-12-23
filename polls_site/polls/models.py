from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question

class Answer(models.Model):
    question    = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.CharField(max_length=50)
    phone_num   = models.CharField(max_length=15)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return self.choice_text
