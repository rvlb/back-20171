from django.shortcuts import render
from django.views.generic import FormView

from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage

from .forms import ContactForm

from core.mixins import (
    NavbarMixin,
)

class ContactFormView(FormView, NavbarMixin):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('core:index')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['message']

        message = EmailMessage(
            subject,
            body,
            to=[email],
        )
        message.send()

        return super(ContactFormView, self).form_valid(form)
