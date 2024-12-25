from django.shortcuts import render
from django.views.generic import TemplateView

from ss_backend.apps.howto.models import Note


class HowToView(TemplateView):
    template_name = "pages/howto.html"
    content_type = "text/html"

    def get(self, request, *args, **kwargs):
        qs = Note.objects.all()
        return render(request, self.template_name, {"notes": qs})
