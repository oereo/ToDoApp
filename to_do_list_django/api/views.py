from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    now_person = Post.object.get(id=id)
    serializer = PostSerializer(now_person)
    return Response("hello world!")