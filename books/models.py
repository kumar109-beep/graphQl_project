from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    title = models.CharField(max_length=100,default="New Quiz")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    SCALE = (
        (0,('Fundamental')),
        (1,('Beginner')),
        (2,('Intermediate')),
        (3,('Advanced')),
        (4,('Expert')),
    )

    TYPE = (
        (0,('Multiple Choice')),
    )

    quiz = models.ForeignKey(Quizzes,on_delete=models.CASCADE)
    technique = models.IntegerField(choices=TYPE,default=0,verbose_name="Type of Question")
    title = models.CharField(max_length=50,verbose_name="Question")
    difficulty = models.IntegerField(choices=SCALE,default=0,verbose_name="Difficulty Level")
    timeStamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False,verbose_name='Active Status')

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answerText = models.CharField(max_length=200,verbose_name="Answer Text")
    is_right = models.BooleanField(default=False)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answerText