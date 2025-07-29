from django.conf import settings as django_settings

__all__ = ["settings"]


class LazySettings:
    HIJACK_PERMISSION_CHECK = "hijack.permissions.superusers_only"
    HIJACK_INSERT_BEFORE = "</body>"
    HIJACK_LOGIN_REDIRECT_URL = django_settings.LOGIN_REDIRECT_URL
    HIJACK_LOGOUT_REDIRECT_URL = django_settings.LOGOUT_REDIRECT_URL

    def __getattribute__(self, name):
        try:
            return getattr(django_settings, name)
        except AttributeError:
            return super().__getattribute__(name)


settings = LazySettings()
