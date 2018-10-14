<template>
<div class="f6inject">
    <div class="off-canvas position-left" v-bind:class="{'is-open': panelVisible}">
        <loginPanel v-if="panel == 'login'" v-on:showPanel="showPanel" v-bind:parkourdexUrl="parkourdexUrl" v-on:login="updateLogin"/>
        <settingsPanel v-if="panel == 'settings'" v-on:showPanel="showPanel" v-bind:parkourdexUrl="parkourdexUrl" v-bind:user="login" v-on:login="updateLogin"/>
        <editPanel v-if="panel == 'edit'" v-on:showPanel="showPanel" v-on:toggleMode="toggleMode" v-bind:parkourdexUrl="parkourdexUrl" v-bind:features="features" v-bind:categories="categories"/>
        <detailPanel v-if="panel == 'detail'" v-on:showPanel="showPanel"/>
        <filterPanel v-if="panel == 'filters'" v-on:showPanel="showPanel" v-on:updateFilters="updateFilters" v-bind:options="filterOptions" v-bind:features="features" v-bind:categories="categories"/>
    </div>
    <div class="off-canvas-content has-transition-push has-position-left grid-y grid-frame" v-bind:class="{'is-open-left': panelVisible}">
        <LMap ref="map" v-bind:attributionControl="false" v-bind:zoom="zoom" v-bind:center="center" v-bind:options="options">
            <LTileLayer v-bind:url="basemapUrl"/>
            <LMarker v-if="myCoords" v-bind:lat-lng="myCoords" v-bind:icon="myIcon">
                <LTooltip v-bind:content="`(${myCoords.lat}, ${myCoords.lng}) ±${myAccuracy}m`"/>
            </LMarker>
            <LCircle v-if="myAccuracy" v-bind:lat-lng="myCoords" v-bind:radius="myAccuracy" v-bind:opacity="0.3" color="#ce5c00" v-bind:fillOpacity="0.10" fillColor="#ce5c00"/>
            
            <LMarker v-for="loc in locations" v-bind:key="loc.id" v-bind:lat-lng="loc.location" v-bind:icon="locIcon">
                <LTooltip v-bind:content="loc.name"/>
            </LMarker>

            <LMarker v-if="(mode == 'add')|(mode == 'addDetail')" v-bind:lat-lng="addPos" v-bind:icon="addIcon" v-bind:draggable="mode == 'add'" />
            

            <div class="controls-topright button-group stacked" v-show="mode == 'default'">
                <button v-if="!loggedIn" class="button expanded" v-on:click="togglePanel('login')">Sign in</button>
                <button v-else class="button expanded" v-on:click="togglePanel('settings')">Settings</button>
                <button class="button expanded" v-bind:class="{ disabled: !loggedIn }" v-on:click="toggleMode('add')">Add spot</button>
                <button class="button expanded" v-on:click="togglePanel('filters')">Filters</button>
                <button class="button expanded" v-on:click="toggleGPS" v-bind:class="{ warning: gpsEnabled && !gpsConnected, success: gpsEnabled && gpsConnected }">Find me</button>
            </div>
            <div class="controls-topright button-group stacked" v-show="mode == 'add'">
                <button class="button expanded" v-on:click="toggleMode('addDetail')">Save</button>
                <button class="button expanded" v-on:click="toggleMode('default')">Cancel</button>
            </div>
            <div class="controls-bottom callout alert" v-show="alertVisible">
                <div>{{ alert }}</div>
                <button class="close-button" aria-label="Dismiss alert" type="button" v-on:click="alertVisible = false">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="controls-bottom callout success" v-show="mode == 'add'">
                <div>Move the green pin to the exact spot you wish to add.</div>
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
        position: fixed;
        top: 1em;
        right: 1em;
        z-index: 2000;
    }

    .controls-bottom {
        display: block;
        position: fixed;
        max-width: 800px;
        left: 1em;
        right: 1em;
        bottom: 8em;
        margin: 0 auto;
        z-index: 2000;
    }


}

</style>
<script>

import loginPanel from './loginPanel.vue';
import settingsPanel from './settingsPanel.vue';
import editPanel from './editPanel.vue';
import detailPanel from './detailPanel.vue';
import filterPanel from './filterPanel.vue';
import { fetchFeatureCategories, fetchLocations, fetchLogin } from './api.js';

import { LMap, LTileLayer, LMarker, LTooltip, LCircle } from 'vue2-leaflet';
import L from 'leaflet';

import '../foundation-min.scss';
import '../leaflet.scss';

import gpsIconUrl from './assets/gps.svg';
import locIconUrl from './assets/pin.svg';
import newIconUrl from './assets/new.svg';


export default {
    name: 'mainComponent',
    components: {
        loginPanel,
        settingsPanel,
        editPanel,
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
            locIcon: new L.Icon({
                iconUrl: `${this.parkourdexUrl}${locIconUrl}`,
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -20],
            }),
            addIcon: new L.Icon({
                iconUrl: `${this.parkourdexUrl}${newIconUrl}`,
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -20],
            }),

            myCoords: null,
            myAccuracy: null,
            panel: null,
            panelVisible: false,
            filterOptions: {
                showAll: true
            },
            categories: [],
            features: [],
            locations: [],
            alert: '',
            alertVisible: false,
            mode: 'default',
            addPos: null,
            editLocation: {
                id: null,
                name: '',
                description: '',
                features: []
            },
            login: {
                email: null,
                username: null,
            },
        };
    },
    computed: {
        loggedIn: function () {
            return this.login.username != null;
        },
        gpsEnabled: function () {
            return this.gpsWatch != null;
        },
        gpsConnected: function () {
            return this.gpsPosition != null;
        },
        filteredLocations: function () {
            return this.locations;
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
        showPanel: function (panel_id, source) {
            this.togglePanel(panel_id);
        },
        toggleMode: function (mode) {
            this.mode = mode;
            if (mode == 'add') {
                this.addPos = L.latLng(this.center.lat, this.center.lng);
            } else if (mode == 'addDetail') {
                this.togglePanel('edit');
            } else if (mode == 'default') {
                this.panelVisible = false;
                this.updateWindow();
            }
        },
        togglePanel: function (panel_id) {
            this.panelVisible = (this.panel != panel_id) | (!this.panelVisible);
            this.panel = panel_id;
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
                    vm.alert = `Geolocation failure: ${err.code} (${err.message})`;
                    vm.alertVisible = true;
                }, {
                    enableHighAccuracy: true,
                    maximumAge: 300
                });
            }
        },
        updateFilters: function (type, index, state) {
            var vm = this;
            if (type == 'category') {
                vm.categories[index].enabled = state;
                vm.categories[index].features.forEach(function (el) {
                    vm.features[el].enabled = state;
                });
            } else if (type == 'feature') {
                vm.features[index].enabled = state;
            } else if (type == 'options') {
                if (index == 'showAll') {
                    vm.filterOptions[index] = state;
                    vm.categories.forEach(function (el) {
                        el.enabled = state;
                    });
                    vm.features.forEach(function (el) {
                        el.enabled = state;
                    });
                }
            }
        },
        updateLogin: function (creds) {
            this.login.email = creds.email
            this.login.username = creds.username;
            if ((this.panel == 'login')|(this.panel == 'settings')) {
                this.panelVisible = false;
            }
        },
        update: function () {
            var vm = this;
            fetchLogin(vm.parkourdexUrl, vm.updateLogin, function (error) {
                console.log(error);
            });
            fetchFeatureCategories(vm.parkourdexUrl, function (data) {
                vm.features = data.features;
                vm.categories = data.categories;
            }, function (error) {
                console.log(error);
            });
            fetchLocations(vm.parkourdexUrl, function (data) {
                vm.locations = data;
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
        this.basemapUrl = this.getMapboxUrl('mapbox.outdoors');
        this.update();
    }
}
</script>
