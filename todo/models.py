from django.db import models


class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField
    #ユーザーリストを外部キーとする
    pic=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
        )
# Create your models here.
