from django.db import models

class Hobby(models.Model):
    title = models.CharField('Nome', max_length=120)
    color = models.CharField('Cor', max_length=7)

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.title
