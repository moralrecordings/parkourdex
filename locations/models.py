from django.conf import settings

from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from simple_history.models import HistoricalRecords

import os


class Base( models.Model ):
    created_by = models.ForeignKey( get_user_model(), null=True, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_created' )
    created_on = models.DateTimeField( auto_now_add=True )
    modified_by = models.ForeignKey( get_user_model(), null=True, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_modified' )
    modified_on = models.DateTimeField( auto_now=True )
    history = HistoricalRecords()

    @property
    def _history_user( self ):
        return self.modified_by

    @_history_user.setter
    def _history_user( self, value ):
        self.modified_by = value

    @property
    def _history_date( self ):
        return self.modified_on

    @_history_date.setter
    def _history_date( self, value ):
        self.modified_on = value

    class Meta:
        abstract = True


class FeatureCategory( Base ):
    name = models.CharField( max_length=256, unique=True )

    def __str__( self ):
        return self.name


class Feature( Base ):
    name = models.CharField( max_length=256, unique=True )
    description = models.TextField()
    category = models.ForeignKey( FeatureCategory, null=True, related_name='features', on_delete=models.SET_NULL )
    icon = models.FileField()

    def __str__( self ):
        return self.name


class Location( Base ):
    name = models.CharField( max_length=256 )
    location = models.PointField()
    description = models.TextField()
    features = models.ManyToManyField( Feature, related_name='locations', blank=True )

    def __str__( self ):
        return self.name


class LocationStatus( Base ):
    user = models.ForeignKey( get_user_model(), related_name='location_statuses', on_delete=models.CASCADE )
    location = models.ForeignKey( Location, related_name='location_statuses', on_delete=models.CASCADE )
    last_visit = models.DateTimeField( null=True )
    favourite = models.BooleanField( default=False )
    shortlist = models.BooleanField( default=False )

    class Meta:
        unique_together = ('user', 'location')


class Comment( Base ):
    location = models.ForeignKey( Location, null=True, related_name='comments', on_delete=models.SET_NULL )
    comment = models.TextField()


def get_photo_path( instance, filename ):
    return os.path.join( 'photos', str( instance.id ), filename )


class Photo( Base ):
    location = models.ForeignKey( Location, null=True, related_name='photos', on_delete=models.SET_NULL )
    photo = models.ImageField( upload_to=get_photo_path )
    thumbnail = ImageSpecField( source='photo', processors=[ResizeToFill(640, 480)] )

