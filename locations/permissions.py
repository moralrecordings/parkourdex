
from rest_framework import permissions


class AuthorOrAdmin( permissions.BasePermission ):
    def has_permission( self, request, view ):
        return self.permission_test( request.user )

    def has_object_permission( self, request, view, obj ):
        return self.object_permission_test( request.user, obj )

    def permission_test( self, user ):
        return user and user.is_authenticated

    def object_permission_test( self, user, obj ):
        return user and (user.is_superuser or (user == obj.created_by))


class SafeAuthorOrAdmin( AuthorOrAdmin ):
    def has_permission( self, request, view ):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission( request, view )

    def has_object_permission( self, request, view, obj ):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_object_permission( request, view, obj )
