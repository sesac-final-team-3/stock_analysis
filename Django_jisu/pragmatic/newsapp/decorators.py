from django.http import HttpResponseForbidden

from newsapp.models import News


def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = News.objects.get(pk=kwargs['pk'])
        # if not project.writer == request.user:
        #     return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
