from django.shortcuts import render
from .models import TodoModel,SubjectModel
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

def home(request):
    return render(request,'home.html')
    
class TodoView(ListView):
    model=TodoModel
    template_name='list.html'
    
    #get_context_dataのオーバーライド
    #プルダウンに渡す辞書キーの追加
    def get_context_data(self,**kwargs):
        #contextは辞書型配列
        context=super(TodoView,self).get_context_data(**kwargs)
        subjects=SubjectModel.objects.all()
        context['subjects']=subjects
        return context
    
    #絞り込み処理の為のクエリセット
    def get_queryset(self):
        #デフォルトではTodoモデルを全取得
        results=self.model.objects.all()
        
        #フォームのGETメソッドから値を取得
        results_sub=self.request.GET.get('subjectfilter')
        
        if results_sub is not None:#GETメソッドから値が取得された時・・・
            results=results.filter(subject=results_sub)
        return results
        
            


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