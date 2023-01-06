from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from projectapp.decorators import project_ownership_required
from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 16

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)



@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = 'target_project'
    form_class = ProjectCreationForm
    template_name = 'projectapp/update.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = 'target_project'
    success_url = reverse_lazy('projectapp:list')
    template_name = 'projectapp/delete.html'

    
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Project.objects.all().order_by('pk')