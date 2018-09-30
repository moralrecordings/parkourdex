<template>
<div class="f6inject">
    <div class="off-canvas position-left" v-bind:class="{'is-open': panelEnabled}">
        <aboutPanel v-if="panel == 'about'" v-on:showPanel="showPanel"/>
        <detailPanel v-if="panel == 'detail'" v-on:showPanel="showPanel"/>
        <filterPanel v-if="panel == 'filters'" v-on:showPanel="showPanel"/>
    </div>
    <div class="off-canvas-content has-transition-push has-position-left grid-y grid-frame" v-bind:class="{'is-open-left': panelEnabled}">
        <LMap ref="map" v-bind:attributionControl="false" v-bind:zoom="zoom" v-bind:center="center" v-bind:options="options">
            <LTileLayer v-bind:url="basemapUrl"/>
            <LMarker v-if="myCoords" v-bind:lat-lng="myCoords" v-bind:icon="myIcon"/>
            <LCircle v-if="myAccuracy" v-bind:lat-lng="myCoords" v-bind:radius="myAccuracy" v-bind:opacity="0.3" color="#ce5c00" v-bind:fillOpacity="0.10" fillColor="#ce5c00"/>
            <div class="controls-topright button-group stacked">
                <button class="button expanded" v-on:click="togglePanel('about')">parkourdex v0.1</button>
                <button class="button expanded" v-on:click="togglePanel('filters')">filters</button>
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
    
    .controls-topright {
        width: 150px;
        display: block;
        position: absolute;
        top: 1em;
        right: 1em;
        z-index: 2000;
    }

}

</style>
<script>

import aboutPanel from './aboutPanel.vue';
import detailPanel from './detailPanel.vue';
import filterPanel from './filterPanel.vue';
import { fetchFeatureCategories } from './api.js';

import { LMap, LTileLayer, LMarker, LTooltip, LCircle } from 'vue2-leaflet';
import L from 'leaflet';

import '../foundation-min.scss';
import '../leaflet.scss';

import gpsIconUrl from './assets/gps.svg';


export default {
    name: 'mainComponent',
    components: {
        aboutPanel,
        detailPanel,
        filterPanel,
        LMap,
        LTileLayer,
        LMarker,
        LTooltip,
        LCircle,
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
            panel: null,
        };
    },
    computed: {
        panelEnabled: function () {
            return this.panel != null;
        },
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
        showPanel: function (ev, panel_id, source) {
            this.togglePanel(panel_id);
        },
        togglePanel: function (panel_id) {
            this.panel = this.panel == panel_id ? null : panel_id;
            this.updateWindow();
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
        update: function () {
            var vm = this;
            fetchFeatureCategories(this.parkourdexUrl, function (data) {
                vm.categories = data;
            }, function (error) {
                console.log(error);
            });
        },
        updateWindow: function () {
            this.$nextTick(function () {
                this.$refs.map.mapObject.invalidateSize();
            });
        },
    },
    mounted: function () {
        this.basemapUrl = this.getMapboxUrl( 'mapbox.outdoors' );
        this.update();
    }
}
</script>
