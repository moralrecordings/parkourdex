from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class Backend( ModelBackend ):
    def authenticate( self, request, username=None, password=None, **kwargs ):
        if username is None:
            username = kwargs.get( UserModel.USERNAME_FIELD )
        try:
            user = None
            if '@' in username:
                user = UserModel.objects.filter(email=username).first()
            if user is None:
                user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password( password )
        else:
            if user.check_password( password ) and self.user_can_authenticate( user ):
                return user
