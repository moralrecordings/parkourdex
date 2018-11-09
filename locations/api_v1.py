from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, serializers, status, generics, views
from rest_framework.decorators import detail_route, list_route, renderer_classes, authentication_classes, permission_classes

from locations.models import Feature, FeatureCategory, Location, LocationStatus

from locations.permissions import AuthorOrAdmin

class FeatureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'category', 'icon')


class FeatureViewSet( viewsets.ReadOnlyModelViewSet ):
    queryset = Feature.objects.order_by( 'name' )
    serializer_class = FeatureSerializer
    permission_classes = (AuthorOrAdmin,)


class FeatureInnerListSerializer( serializers.ListSerializer ):
    def to_representation( self, data, *argc, **argv ):
        return super().to_representation( data.order_by( 'name' ), *argc, **argv )


class FeatureInnerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'icon')
        list_serializer_class = FeatureInnerListSerializer


class FeatureCategorySerializer( serializers.ModelSerializer ):
    features = FeatureInnerSerializer( many=True )
    class Meta:
        model = FeatureCategory
        fields = ('id', 'name', 'features')


class FeatureCategoryViewSet( viewsets.ReadOnlyModelViewSet ):
    queryset = FeatureCategory.objects.prefetch_related( 'features' ).order_by( 'name' )
    serializer_class = FeatureCategorySerializer
    permission_classes = (AuthorOrAdmin,)


class LocationListSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Location
        fields = ('id', 'name', 'features', 'location')


class LocationSerializer( serializers.Serializer ):
    class Meta:
        model = Location
        fields = ('id', 'name', 'features', 'location', 'description', 'photos', 'editable', 'visit')

    editable = serializers.SerializerMethodField()
    visit = serializers.SerializerMethodField()

    def get_editable( self, obj ):
        request = self.context.get( 'request' )
        return AuthorOrAdmin().object_permission_test( request.user, obj )

    def get_visit( self, obj ):
        request = self.context.get( 'request' )
        return obj.visits.filter( user=request.user ).first()


class LocationStatusSerializer( serializers.ModelSerializer ):
    class Meta:
        model = LocationStatus
        fields = ('last_visit', 'favourite', 'shortlist')


class LocationStatusViewSet( viewsets.ModelViewSet ):
    serializer_class = LocationStatusSerializer
    permission_classes = (AuthorOrAdmin,)

    def get_queryset( self ):
        return LocationStatus.objects.filter( user=self.request.user, location=self.kwargs['location_pk'] )
        

class LocationViewSet( viewsets.ModelViewSet ):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    list_serializer_class = LocationListSerializer
    permission_classes = (AuthorOrAdmin,)

    # for the top level GET, use the minimum detail version of each record
    def get_serializer( self, *args, **kwargs ):
        if 'many' in kwargs:
            serializer_class = self.list_serializer_class
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class( *args, **kwargs )



