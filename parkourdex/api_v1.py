from django.conf.urls import include, url
from rest_framework import routers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from parkourdex.views import LoginView, LogoutView
from locations.api_v1 import FeatureViewSet, FeatureCategoryViewSet, LocationViewSet

# borrowed from https://stackoverflow.com/questions/18818179/routing-api-views-in-django-rest-framework#18823752
class Router(routers.DefaultRouter):
    """
    Extends functionality of DefaultRouter adding possibility
    to register simple API views, not just Viewsets.
    """

    def get_routes(self, viewset):
        """
        Checks if the viewset is an instance of ViewSet,
        otherwise assumes it's a simple view and does not run
        original `get_routes` code.
        """
        if issubclass(viewset, viewsets.ViewSetMixin):
            return super().get_routes(viewset)

        return []

    def get_urls(self):
        """
        Append non-viewset views to the urls
        generated by the original `get_urls` method.
        """    
        # URLs for simple views
        ret = []
        for prefix, viewset, basename in self.registry:

            # Skip viewsets
            if issubclass(viewset, viewsets.ViewSetMixin):
                continue

            # URL regex
            regex = '{prefix}{trailing_slash}$'.format(
                prefix=prefix,
                trailing_slash=self.trailing_slash
            )

            # The view name has to have suffix "-list" due to specifics
            # of the DefaultRouter implementation.
            ret.append(url(
                regex, viewset.as_view(),
                name='{0}-list'.format(basename)
            ))

        # Format suffixes
        ret = format_suffix_patterns(ret, allowed=['json', 'html'])

        # Prepend URLs for viewsets and return
        return super().get_urls() + ret


api_v1_router = Router()
api_v1_router.register('login', LoginView, base_name='login')
api_v1_router.register('logout', LogoutView, base_name='logout')
api_v1_router.register('feature', FeatureViewSet)
api_v1_router.register('feature_category', FeatureCategoryViewSet)
api_v1_router.register('location', LocationViewSet)

