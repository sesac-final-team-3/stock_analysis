from django.http import HttpResponseForbidden

from projectapp.models import Project


def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        # if not project.writer == request.user:
        #     return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
