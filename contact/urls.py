from django.conf.urls import url

from .views import ContactFormView

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name='email'),
]
