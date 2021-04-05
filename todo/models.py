from django.db import models

class SubjectModel(models.Model):
    subjects=models.CharField(verbose_name="科目",max_length=25)
    
    def __str__(self):
        return self.subjects
        

class TodoModel(models.Model):
    subject=models.ForeignKey('SubjectModel',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    #ユーザーリストを外部キーとする
    pic=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
        )
# Create your models here.
