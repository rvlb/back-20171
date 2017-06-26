from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, required=True)
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    subject = forms.CharField(label='Assunto', max_length=100, required=True)
    message = forms.CharField(
        label='Mensagem',
        max_length=200,
        widget=forms.Textarea,
        required=True
    )
