from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Profile, Comment
from .forms import PostForm, EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
# def home(request):
#     return render(request, 'home.html', {})

# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post.id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering =['-id']
    ordering = ['-date']
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html' ,{'cat_menu_list': cat_menu_list})
    

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '),'category_posts' : category_posts})
    


class ArticleDetailView(DetailView):
    model = Post
    template_name = "acticle_details.html"

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCommentView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

# class UpdateAvatar(UpdateView):
#     model = Profile
#     template_name = 'update_avatar.html'
#     fields=('profile_pic')
    
# class SearchResultsView(ListView):
#     model = Post
#     template_name = 'search_results.html'

#     def get_queryset(self):
#         qs = super(SearchResultsView,self).get_queryset()
#         search_results = qs.filter(title__icontains=self.kwargs['title'])
#         return search_results

def SearchResultsView(request):
    query = request.GET.get('q')
    search_results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(category__icontains=query) |
        Q(body__icontains=query)
        )
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})
    
    
