from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import AnimalModel
from .serializers import AnimalSerializer


class IsSuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class AnimalCreateAPIView(generics.CreateAPIView):
    serializer_class = AnimalSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]


class AnimalUpdateAPIView(generics.UpdateAPIView):
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AnimalListAPIView(generics.ListAPIView):
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AnimalRetrieveAPIView(generics.RetrieveAPIView):
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AnimalDeleteAPIView(generics.DestroyAPIView):
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated, IsSuperuserPermission]
    authentication_classes = [JWTAuthentication]
