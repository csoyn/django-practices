from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # pip install Pillow => 이미지를 조작하기 위한 라이브러리
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
