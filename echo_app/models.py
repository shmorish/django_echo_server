from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  # 投稿のタイトル
    content = models.TextField()             # 投稿の内容
    created_at = models.DateTimeField(auto_now_add=True)  # 投稿日時

    def __str__(self):
        return self.title