from django.db import models
from django.conf import settings

# articles_article 테이블이 생성됨!
class Article(models.Model):
    # 1 : N  => user : article
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # M : N =>
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# articles_comment 테이블이 생성됨!
class Comment(models.Model):
    # 1 : N => article : comment
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # 1 : N => user : comment
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)