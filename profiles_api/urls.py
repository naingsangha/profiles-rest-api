from django.urls import path, include

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

from profiles_api import views

urlpatterns = [
     path('hello-view/', views.HelloApiView.as_view()), 
]
