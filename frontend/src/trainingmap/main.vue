<template>
<div class="f6inject">
    <div class="off-canvas position-left reveal-for-medium is-open">
        <detailPanel/>
    </div>
    <div class="off-canvas-content is-open-left has-position-left has-transition-push grid-y grid-frame">
        <l-map ref="map" v-bind:attributionControl="false" v-bind:zoom="zoom" v-bind:center="center" v-bind:options="options">
            <l-tile-layer v-bind:url="basemapUrl"/>
        </l-map>
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

}

</style>
<script>

import detailPanel from './detailPanel.vue';
import { LMap, LTileLayer, LMarker, LTooltip } from 'vue2-leaflet';
import L from 'leaflet';

import '../foundation-min.scss';
import '../leaflet.scss';

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
            },
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
