from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),

    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('update/', ProjectUpdateView.as_view(), name='update'),
    path('delete/', ProjectDeleteView.as_view(), name='delete'),
]