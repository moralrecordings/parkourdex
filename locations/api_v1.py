from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, serializers, status, generics, views
from rest_framework.decorators import detail_route, list_route, renderer_classes, authentication_classes, permission_classes

from locations.models import Feature, FeatureCategory


class FeatureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'category', 'icon')


class FeatureViewSet( viewsets.ReadOnlyModelViewSet ):
    queryset = Feature.objects.order_by( 'name' )
    serializer_class = FeatureSerializer


class FeatureInnerListSerializer( serializers.ListSerializer ):
    def to_representation( self, data, *argc, **argv ):
        return super().to_representation( data.order_by( 'name' ), *argc, **argv )


class FeatureInnerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'icon')
        list_serializer_class = FeatureInnerListSerializer


class FeatureCategorySerializer( serializers.ModelSerializer ):
    features = FeatureInnerSerializer(many=True)
    class Meta:
        model = FeatureCategory
        fields = ('id', 'name', 'features')


class FeatureCategoryViewSet( viewsets.ReadOnlyModelViewSet ):
    queryset = FeatureCategory.objects.prefetch_related( 'features' ).order_by( 'name' )
    serializer_class = FeatureCategorySerializer
