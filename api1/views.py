from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from post.models import post
from .serializer import PostDeleteSerializer,PostDetailSerializer,PostListSerializer,PostUpdateSerializer


class DeleteView(DestroyAPIView):
	queryset = post.objects.all()
	serializer_class = PostDeleteSerializer


class DetailView(RetrieveAPIView):
	queryset = post.objects.all()
	serializer_class = PostDetailSerializer


class ListView(ListAPIView):
	queryset = post.objects.all()
	serializer_class = PostListSerializer


class UpdateView(UpdateAPIView):
	queryset = post.objects.all()
	serializer_class = PostUpdateSerializer
