from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Books(models.Model):
    title = models.CharField('Название книги', max_length=64)
    author = models.ForeignKey(
        "Authors", on_delete=models.CASCADE, related_name='authos_book')
    description = models.CharField('Описание книги', max_length=250)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Authors(models.Model):
    firs_name = models.CharField('Имя автора', max_length=64)
    last_name = models.CharField('Фамилия автора', max_length=64)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.firs_name} {self.last_name}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
