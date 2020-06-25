from django.shortcuts import render
from rest_framework import viewsets
from .models import User,ActivityPeriod
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def UserList(request):
    user_list=User.objects.all()
    serializer=UserSerializer(user_list,many=True)
    return Response(serializer.data)
