from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, serializers, status, generics, views
from rest_framework.decorators import action, renderer_classes, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from locations.models import Feature, FeatureCategory, Location, LocationStatus

from locations.permissions import SafeAuthorOrAdmin, AuthorOrAdmin

class FeatureSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'category', 'icon')


class FeatureViewSet( viewsets.ReadOnlyModelViewSet ):
    queryset = Feature.objects.order_by( 'name' )
    serializer_class = FeatureSerializer
    permission_classes = (SafeAuthorOrAdmin,)


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
    permission_classes = (SafeAuthorOrAdmin,)


class LocationStatusSerializer( serializers.ModelSerializer ):
    class Meta:
        model = LocationStatus
        fields = ('last_visit', 'favourite', 'shortlist')


class LocationStatusView( generics.RetrieveUpdateAPIView ):
    serializer_class = LocationStatusSerializer
    permission_classes = (AuthorOrAdmin,)

    def get_object( self ):
        return LocationStatus.objects.filter( user=self.request.user, location=self.kwargs['location_pk'] ).first()

    def list( self, request, *args, **kwargs ):
        obj = self.get_object()
        serial = self.get_serializer_class()( obj )
        return Response( serial.data )

    def update( self, request, *args, **kwargs ):
        partial = kwargs.get( 'partial', False )
        instance, _ = LocationStatus.objects.get_or_create( user=request.user, location=self.kwargs['location_pk'] )
        serial = LocationStatusSerializer( instance, data=request.data, partial=partial )
        serial.is_valid( raise_exception=True )
        serial.save()
        return Response( serial.data )

    def partial_update( self, request, *args, **kwargs ):
        kwargs['partial'] = True
        return self.update( request, *args, **kwargs )


class LocationListSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Location
        fields = ('id', 'name', 'features', 'location')


class LocationSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Location
        fields = ('id', 'name', 'features', 'location', 'description', 'editable', 'status')

    editable = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_editable( self, obj ):
        request = self.context.get( 'request' )
        return AuthorOrAdmin().object_permission_test( request.user, obj )

    def get_status( self, obj ):
        request = self.context.get( 'request' )
        status = LocationStatus.objects.filter( user=request.user, location=obj ).first()
        serial = LocationStatusSerializer( status )
        return serial.data


class LocationViewSet( viewsets.ModelViewSet ):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    list_serializer_class = LocationListSerializer
    permission_classes = (SafeAuthorOrAdmin,)

    def get_serializer( self, *args, **kwargs ):
        if 'many' in kwargs:
            serializer_class = self.list_serializer_class
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class( *args, **kwargs )

