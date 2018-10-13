from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication, permission

class WhoAmI( APIView ):
    permission_classes = permission.AllowAny

    def get( self, request, format=None ):
        result = {}
        if request.user.is_anonymous:
            result['email'] = None
        else:
            result['email'] = request.user.email
        return Response( result )
