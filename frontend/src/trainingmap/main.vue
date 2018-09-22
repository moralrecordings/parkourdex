<template>
<div class="f6inject">
    <div class="grid-y grid-frame">
        <l-map ref="map" v-bind:attributionControl="false" v-bind:zoom="zoom" v-bind:center="center">
            <l-tile-layer v-bind:url="basemapUrl"/>
        </l-map>
    </div>
</div>
</template>
<style>

</style>
<script>

import { LMap, LTileLayer, LMarker, LTooltip } from 'vue2-leaflet';
import L from 'leaflet';

import '../foundation-min.scss';
import '../leaflet.scss';

export default {
    name: 'mainComponent',
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LTooltip,
    },
    data: function () {
        return {
            zoom: 5,
            center: L.latLng(-24.966, 123.750),
            basemapUrl: null,
        };
    },
    props: {
        parkourdexUrl: String,
        mapboxToken: String,
    },
    methods: {
        getMapboxUrl: function (layer_id) {
            return `https://api.mapbox.com/v4/${layer_id}/{z}/{x}/{y}.png256?access_token=${this.mapboxToken}`;
        }
    },
    mounted: function () {
        this.basemapUrl = this.getMapboxUrl( 'mapbox.outdoors' );
    }
}
</script>
