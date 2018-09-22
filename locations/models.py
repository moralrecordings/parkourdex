from django.conf import settings

from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

from simple_history.models import HistoricalRecords

import os


class Base( models.Model ):
    created_by = models.ForeignKey( get_user_model(), null=True, on_delete=models.SET_NULL )
    created_on = models.DateTimeField( auto_now_add=True )
    modified_by = models.ForeignKey( get_user_model(), null=True, on_delete=models.SET_NULL )
    modified_on = models.DateTimeField()
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
    def _history_date( self, value )
        self.modified_on = value

    class Meta:
        abstract = True


class TrainingFeature( Base ):
    name = models.CharField( max_length=256, unique=True )
    description = models.TextField()
    icon = models.ImageField()


class TrainingSpot( Base ):
    name = models.CharField( max_length=256 )
    location = models.PointField()
    description = models.TextField()
    features = models.ManyToManyField( TrainingFeature, related_name='spots' )


class TrainingLore( Base ):
    lore = models.TextField()


def get_photo_path( instance, filename ):
    return os.path.join( 'photos', str( instance.id ), filename )


class Photo( Base ):
    training_spot = models.ForeignKey( TrainingSpot, null=True, related_name='photos' )
    photo = models.ImageField( upload_to=get_photo_path )


