from django.conf.urls import include, url
from rest_framework import routers

from parkourdex.views import WhoAmIView
from locations.api_v1 import FeatureViewSet, FeatureCategoryViewSet, LocationViewSet

api_v1_router = routers.DefaultRouter()
api_v1_router.register('whoami', WhoAmIView)
api_v1_router.register('feature', FeatureViewSet)
api_v1_router.register('feature_category', FeatureCategoryViewSet)
api_v1_router.register('location', LocationViewSet)

