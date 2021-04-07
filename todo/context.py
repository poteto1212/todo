from .models import SubjectModel

#テンプレートにカテゴリデータを渡す
def related(request):
    context={
        'category_list':SubjectModel.objects.all(),
    }
    return context