# import templateview

from django.urls import path
from django.views.generic import TemplateView

from ss_backend.apps.howto.views import HowToView

app_name = "howto"
urlpatterns = [
    path("", HowToView.as_view(), name="howto"),
]
