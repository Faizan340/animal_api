from django.contrib import admin
from django.urls import path
from .views import AnimalCreateAPIView, AnimalUpdateAPIView, AnimalRetrieveAPIView, AnimalListAPIView, AnimalDeleteAPIView

urlpatterns = [
    path('create/', AnimalCreateAPIView.as_view(), name='animal_create'),
    path('update/<int:pk>/', AnimalUpdateAPIView.as_view(), name='animal_update'),
    path('list/', AnimalListAPIView.as_view(), name='animal_list'),
    path('retrieve/<int:pk>/', AnimalRetrieveAPIView.as_view(), name='animal_retrieve'),
    path('delete/<int:pk>/', AnimalDeleteAPIView.as_view(), name='animal_delete')
]
