from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication, permissions


class LoginView( APIView ):
    permission_classes = (permissions.AllowAny,)

    def get( self, request, format=None ):
        result = {
            'username': None,
            'email': None
        }
        if not request.user.is_anonymous:
            result['username'] = request.user.username
            result['email'] = request.user.email
        return Response( result )


    def post( self, request, format=None ):
        if 'username' in request.data and 'password' in request.data:
            username = request.data['username']
            password = request.data['password']
            user = authenticate( request=request, username=username, password=password )
            if user is not None:
                login( request, user )
                result = {
                    'username': user.username,
                    'email': user.email
                }
                return Response( result )
            return Response( {
                'error': 'The username and password do not match.'
            }, status=403 )
        return Response( {
            'error': 'Must specify username and a password.'
        }, status=400 )


class LogoutView( APIView ):
    permission_classes = (permissions.IsAuthenticated,)

    def post( self, request, format=None ):
        logout( request )
        return Response( {
            'username': None,
            'email': None,
        } )
