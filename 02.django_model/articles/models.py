from django.db import models


# article table 생성을 위한 class
# table : articles_article
class Article(models.Model):
    # field
    # pk => django에서는 알아서 관리해준다!
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 0001_initial.py에 작성됨!

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 0002_auto_20210310_1345.py에 작성됨!

    def __str__(self):
        return f'{self.pk}. {self.title}'