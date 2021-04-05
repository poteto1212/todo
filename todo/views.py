from django.shortcuts import render
from .models import TodoModel,SubjectModel
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

def home(request):
    return render(request,'home.html')
    
class TodoView(ListView):
    model=TodoModel
    template_name='list.html'
    
    def get_context_data(self,**kwargs):
        #contextは辞書型配列
        context=super(TodoView,self).get_context_data(**kwargs)
        subjects=SubjectModel.objects.all()
        context['subjects']=subjects
        return context

class Detail(DetailView):
    model=TodoModel
    template_name='detail.html'
    
class TodoCreateView(CreateView):#adminフォームに似た要領で作成
    model=TodoModel
    template_name='create.html'
    fields=['title','content','pic']
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