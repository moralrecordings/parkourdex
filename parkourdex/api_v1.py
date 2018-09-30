from django.conf.urls import include, url
from rest_framework import routers

from locations.api_v1 import FeatureViewSet, FeatureCategoryViewSet

api_v1_router = routers.DefaultRouter()
api_v1_router.register(r'feature', FeatureViewSet)
api_v1_router.register(r'feature_category', FeatureCategoryViewSet)
