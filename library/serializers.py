from rest_framework import serializers
from . import models


class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = ["title", "description", "author"]

    def to_representation(self, instance):
        rep = super(BooksModelSerializer, self).to_representation(instance)
        rep['author'] = f'{instance.author.firs_name} {instance.author.last_name}'
        return rep


class AuthorsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = ["firs_name", "last_name", "date_of_birth"]
