from django.views.generic import (
    TemplateView,
    ListView,
)

from .mixins import (
    NavbarMixin,
)

from .models import Hobby

class IndexView(TemplateView, NavbarMixin):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['name'] = 'Renato'
        return context

class HobbiesView(ListView, NavbarMixin):
    template_name = 'core/hobbies.html'
    model = Hobby
    context_object_name = 'hobbies'

class ContactView(TemplateView, NavbarMixin):
    template_name = 'core/contact.html'
