from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ss_backend.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import ss_backend.users.signals  # noqa: F401
        except ImportError:
            pass
