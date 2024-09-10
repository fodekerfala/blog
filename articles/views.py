from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView
from .forms import FormArticle,FormCategories,CommentForm
from django.db.models import Q
from .models import Articles,Categories,Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class Create_Article(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = FormArticle
    template_name = 'articles/create_article.html'
    success_url = reverse_lazy('articles:article_view')

    def form_valid(self, form):
        form.instance.autor = self.request.user 
        return super().form_valid(form)


class Article_view(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'articles/article_view.html'
    ordering = ['-date_pub']

    def get_queryset(self):
        queryset = Articles.objects.filter(publiche=True)
        
        query = self.request.GET.get('searchvalue')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        else:
            queryset = Articles.objects.filter(publiche=True)
        return queryset
    


class Brouillon_view(LoginRequiredMixin,ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'articles/bruillons.html'

    def get_queryset(self):
        return Articles.objects.filter(publiche=False)


class Update_article(LoginRequiredMixin,UpdateView):
    model = Articles
    form_class = FormArticle
    template_name = 'articles/update_article.html'
    success_url = reverse_lazy('articles:article_view')

class Article_detail(DetailView):
    model = Articles
    context_object_name = 'article'
    template_name = 'articles/view_detail_article.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class Delete_article(LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'articles/confirme_delete_article.html'
    success_url = reverse_lazy('articles:article_view')


class Create_categorie(LoginRequiredMixin,CreateView):
    model = Categories
    fields = ['title']
    template_name = 'articles/categories/create_categorie.html'
    success_url = reverse_lazy('articles:view_categorie')
    
class Update_categorie(LoginRequiredMixin,UpdateView):
    model = Categories
    fields = ['title']
    template_name = 'articles/categories/update_categorie.html'
    success_url = reverse_lazy('view_categorie')
    
class View_categorie(ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'articles/categories/view_categorie.html'
    
class Delete_categorie(LoginRequiredMixin,DeleteView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'articles/categories/delete_categorie.html'
    success_url = reverse_lazy('articles:view_categorie')


def categorieselement(request,categorie):
    queryset = categorie
    articles = Articles.objects.filter(categorie=queryset, publiche= True)

    context = {'articles':articles,
               'categori':queryset
               }
    return render(request,'articles/categories/article_for_categorie.html',context)


def commentaire(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article 
            comment.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = CommentForm() 
    return render(request, 'comment_template.html', {'form': form, 'article': article})


def category_view(request):
    categories = Categories.objects.all()
    return render(request, 'articles/header.html', {'categories': categories})