from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import URL
from .serializer import UrlSerializer, UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class URLViewSet(viewsets.ModelViewSet):
    serializer_class = UrlSerializer
    queryset =URL.objects.all()


class URLDetails(APIView):

    def get_object(self, id):
        try:
            return URL.objects.get(id=id)
        except URL.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND) 

    def get(self, request, id):
        url = self.get_object(id)
        serializer = UrlSerializer(url)
        return Response(serializer.data)

    def put(self, request, id):
        url = self.get_object(id)
        serializer = UrlSerializer(url, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        url = self.get_object(id)
        url.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)