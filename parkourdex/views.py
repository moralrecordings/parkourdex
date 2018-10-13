from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication, permissions

class WhoAmIView( APIView ):
    permission_classes = (permissions.AllowAny,)

    def get( self, request, format=None ):
        result = {}
        if request.user.is_anonymous:
            result['email'] = None
        else:
            result['email'] = request.user.email
        return Response( result )
