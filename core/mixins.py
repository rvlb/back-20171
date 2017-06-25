from django.views.generic.base import ContextMixin

class NavbarMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(NavbarMixin, self).get_context_data(**kwargs)
        context['nav_items'] = [
            { 'title': 'Início', 'url': 'core:index' },
            { 'title': 'Hobbies', 'url': 'core:hobbies' },
            { 'title': 'Contato', 'url': 'core:contact' },
        ]
        return context
