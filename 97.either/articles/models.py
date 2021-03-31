from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.CharField(max_length=200)
    content2 = models.CharField(max_length=200)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    content = models.CharField(max_length=100)