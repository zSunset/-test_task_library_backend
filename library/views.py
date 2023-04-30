from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models


class BooksModelViewSet(ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksModelSerializer


class AuthorsModelViewSet(ModelViewSet):
    queryset = models.Authors.objects.all()
    serializer_class = serializers.AuthorsModelSerializer
