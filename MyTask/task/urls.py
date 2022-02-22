from .views import RegisterAPI, LoginAPI, GenericAPIView, URLDetails    
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('task/register/', RegisterAPI.as_view(), name='register'),
    path('task/login/', LoginAPI.as_view(), name='login'),
    path('task/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('task/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('generic/URL/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', URLDetails.as_view()),
]