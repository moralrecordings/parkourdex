<template>
<div class="f6inject">
    <div class="off-canvas position-left" v-bind:class="{'is-open': showPanel, 'reveal-for-medium': showPanel}">
        <detailPanel/>
    </div>
    <div class="off-canvas-content has-position-left grid-y grid-frame" v-bind:class="{'is-open-left': showPanel}">
        <LMap ref="map" v-bind:attributionControl="false" v-bind:zoom="zoom" v-bind:center="center" v-bind:options="options">
            <LTileLayer v-bind:url="basemapUrl"/>
            <LMarker v-if="myCoords" v-bind:lat-lng="myCoords" v-bind:icon="myIcon"/>
            <div class="controls-topleft">
                <button class="button" v-on:click="toggleAbout">parkourdex v0.1</button>
            </div>
            <div class="controls-topright button-group stacked">
                <button class="button expanded">add spot</button>
                <button class="button expanded" v-on:click="toggleGPS" v-bind:class="{ warning: gpsEnabled && !gpsConnected, success: gpsEnabled && gpsConnected }">find me</button>
            </div>
        </LMap>
    </div>
</div>
</template>
<style lang="scss">



.f6inject {
    .off-canvas {
        padding: 1em;
    }

    .off-canvas label {
        line-height: inherit;
        font-size: inherit;
        font-weight: inherit;
    }
    
    .controls-topleft {
        display: block;
        position: absolute;
        top: 1em;
        left: 1em;
        z-index: 2000;
    }

    .controls-topright {
        width: 100px;
        display: block;
        position: absolute;
        top: 1em;
        right: 1em;
        z-index: 2000;
    }
}

</style>
<script>

import detailPanel from './detailPanel.vue';
import { LMap, LTileLayer, LMarker, LTooltip } from 'vue2-leaflet';
import L from 'leaflet';

import '../foundation-min.scss';
import '../leaflet.scss';

import gpsIconUrl from './assets/gps.svg';


export default {
    name: 'mainComponent',
    components: {
        detailPanel,
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
            options: {
                attributionControl: false,
                zoomControl: false,
            },
            showPanel: false,
            gpsWatch: null,
            gpsPosition: null,
            myIcon: new L.Icon({
                iconUrl: `${this.parkourdexUrl}${gpsIconUrl}`,
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -20],
            }),
            myCoords: null,
            myAccuracy: null,
        };
    },
    computed: {
        gpsEnabled: function () {
            return this.gpsWatch != null;
        },
        gpsConnected: function () {
            return this.gpsPosition != null;
        },
    },
    props: {
        parkourdexUrl: String,
        mapboxToken: String,
    },
    methods: {
        getMapboxUrl: function (layer_id) {
            return `https://api.mapbox.com/v4/${layer_id}/{z}/{x}/{y}.png256?access_token=${this.mapboxToken}`;
        },
        toggleAbout: function () {
            this.showPanel = !this.showPanel;
        },
        toggleGPS: function () {
            var vm = this;
            if (this.gpsEnabled) {
                window.navigator.geolocation.clearWatch(this.gpsWatch);
                this.gpsWatch = null;
            } else {
                this.gpsPosition = null;
                this.gpsWatch = window.navigator.geolocation.watchPosition(function (pos) {
                    vm.gpsPosition = pos;
                    vm.myCoords = L.latLng(pos.coords.latitude, pos.coords.longitude);
                    vm.myAccuracy = pos.coords.accuracy / 2;
                }, function (err) {
                    console.log(err);
                }, {
                    enableHighAccuracy: true,
                    maximumAge: 300
                });
            }
        },
    },
    mounted: function () {
        this.basemapUrl = this.getMapboxUrl( 'mapbox.outdoors' );
    }
}
</script>
