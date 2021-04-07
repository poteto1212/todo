from django.shortcuts import render
from .models import TodoModel,SubjectModel
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

def home(request):
    return render(request,'home.html')
    
class TodoView(ListView):
    model=TodoModel
    template_name='list.html'
    #id降順(投稿の新しい順)にTodoを取得する
    def get_queryset(self):
        queryset=TodoModel.objects.order_by('-id')
        return queryset

#科目選択カテゴリー
class CategoryView(ListView):
    model=TodoModel
    template_name='list.html'
    
    #urlパラメータからのクエリ取得
    def get_queryset(self):
        category=SubjectModel.objects.get(subjects=self.kwargs['category'])#urk名
        queryset=TodoModel.objects.order_by('-id').filter(subject=category)
        return queryset
    
    #受け取ったデータを辞書に   
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category_key']=self.kwargs['category']
        return context

class Detail(DetailView):
    model=TodoModel
    template_name='detail.html'
    
class TodoCreateView(CreateView):#adminフォームに似た要領で作成
    model=TodoModel
    template_name='create.html'
    fields=['subject','title','content','pic']
    success_url=reverse_lazy('list') #投稿後自動的にdetail.htmlに飛ぶ(urlのname引数で指定)
    
class TodoDelete(DeleteView):
    model=TodoModel
    template_name='delete.html'
    success_url=reverse_lazy('list')
    
class TodoUpdateView(UpdateView):
    model=TodoModel
    template_name='update.html'
    fields=['title','content','pic']
    success_url=reverse_lazy('list')