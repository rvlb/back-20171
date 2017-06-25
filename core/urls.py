from django.conf.urls import url

from .views import (
    IndexView,
    HobbiesView,
    ContactView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^hobbies/$', HobbiesView.as_view(), name='hobbies'),
    url(r'^contato/$', ContactView.as_view(), name='contact'),
]
