from django.db import models

#科目選択(1対ｎ)
class SubjectModel(models.Model):
    subjects=models.CharField(verbose_name="作用領域",max_length=25)
    
    def __str__(self):
        return self.subjects
    
    class Meta:
        verbose_name="科目カテゴリー"
#タグ(n対n)
class Field(models.Model):
    fields=models.CharField(verbose_name="作用機序",max_length=50)
    
    def __str__(self):
        return self.fields

#メインデータ
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
    field=models.ManyToManyField('Field',verbose_name='分野')
    relation=models.ManyToManyField('self',verbose_name='関連分野',blank=True,null=True)
    created_at=models.DateField(verbose_name='最終更新日',auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    
    class Meta:
        verbose_name="医薬品データベース"
        verbose_name_plural="医薬品データベース"