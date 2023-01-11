from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from newsapp.decorators import project_ownership_required
from articleapp.models import Article
from newsapp.forms import NewsCreationForm
from newsapp.models import News


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class NewsCreateView(CreateView):
    model = News
    form_class = NewsCreationForm
    template_name = 'newsapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('newsapp:detail', kwargs={'pk': self.object.pk})


class NewsDetailView(DetailView, MultipleObjectMixin):
    model = News
    context_object_name = 'target_project'
    template_name = 'newsapp/detail.html'

    paginate_by = 16




@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class NewsUpdateView(UpdateView):
    model = News
    context_object_name = 'target_project'
    form_class = NewsCreationForm
    template_name = 'newsapp/update.html'

    def get_success_url(self):
        return reverse('newsapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'target_project'
    success_url = reverse_lazy('newsapp:list')
    template_name = 'newsapp/delete.html'

    
class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'newsapp/list.html'
    paginate_by = 3
    

    def get_queryset(self):
        return News.objects.all().order_by('pk')