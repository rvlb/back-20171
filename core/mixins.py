from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin

from django.contrib.auth.forms import AuthenticationForm

class NavbarMixin(FormMixin, ContextMixin):
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super(NavbarMixin, self).get_context_data(**kwargs)
        context['nav_items'] = [
            { 'title': 'Início', 'url': 'core:index', 'id': 'link-index' },
            { 'title': 'Hobbies', 'url': 'core:hobbies', 'id': 'link-hobbies' },
            { 'title': 'Contato', 'url': 'contact:email', 'id': 'link-contact' },
        ]
        return context
