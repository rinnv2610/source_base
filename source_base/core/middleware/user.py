from threading import local

from django.conf import settings
from django.contrib.auth.models import AnonymousUser

USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')

_thread_locals = local()


def _do_set_current_user(user_fun):
    setattr(_thread_locals, USER_ATTR_NAME, user_fun.__get__(user_fun, local))


def _set_current_user(user=None):
    _do_set_current_user(lambda self: user)


class CurrentUserMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _do_set_current_user(lambda self: getattr(request, 'user', None))
        response = self.get_response(request)
        return response


def get_current_user():
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    if callable(current_user):
        return current_user()
    return current_user


def get_current_authenticated_user():
    current_user = get_current_user()
    if isinstance(current_user, AnonymousUser):
        return None
    return current_user