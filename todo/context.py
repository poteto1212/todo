from .models import SubjectModel,Field

#テンプレートにカテゴリデータを渡す
#タグデータも同様に渡す
def related(request):
    context={
        'category_list':SubjectModel.objects.all(),
        'tag_list':Field.objects.all()
    }
    return context
    