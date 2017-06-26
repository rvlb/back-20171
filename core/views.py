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
        context['content'] = [
            { 'title': 'Instalação e criação de um projeto', 'status': True },
            { 'title': 'Model, Template & View', 'status': True },
            { 'title': 'URLs', 'status': True },
            { 'title': 'Admin', 'status': True },
            { 'title': 'Integração Front-end/Back-end', 'status': True },
            { 'title': 'Template tags', 'status': True },
            { 'title': 'Forms', 'status': True },
            { 'title': 'Autenticação (se der tempo)', 'status': True },
            { 'title': 'Django + AJAX (se der tempo)', 'status': True },
        ]
        return context

class HobbiesView(ListView, NavbarMixin):
    template_name = 'core/hobbies.html'
    model = Hobby
    context_object_name = 'hobbies'
