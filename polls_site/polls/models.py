from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_type = models.CharField(max_length=20)
    created_at    = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=50)

    class Meta:
        db_table = 'choices'

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    choice      = models.ForeignKey(Choice, on_delete = models.CASCADE)
    answer_text = models.CharField(max_length=50)
    phone_num   = models.CharField(max_length=15)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return self.answer_text
