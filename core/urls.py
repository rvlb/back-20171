from django.conf.urls import url

from .views import (
    IndexView,
    HobbiesView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^hobbies/$', HobbiesView.as_view(), name='hobbies'),
]
