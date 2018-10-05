from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from locations.models import FeatureCategory, Feature, Location, Comment, Photo

admin.site.register(FeatureCategory, SimpleHistoryAdmin)
admin.site.register(Feature, SimpleHistoryAdmin)
admin.site.register(Location, SimpleHistoryAdmin)
admin.site.register(Comment, SimpleHistoryAdmin)
admin.site.register(Photo, SimpleHistoryAdmin)
