<template>
    <div v-if="detail" class="grid-container full">
        <h3>{{ detail.name }}</h3>
        <div class="grid-x">
            <ul>
                <li v-for="feature in detail.features">
                    <img v-if="featureMap.get(feature) && featureMap.get(feature).icon" v-bind:src="`${parkourdexUrl}${featureMap.get(feature).icon}`" v-bind:title="featureMap.get(feature).name" /> {{ featureMap.get(feature).name }}
                </li>
            </ul>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <gallery ref="gallery">
                    <img src="./assets/photoblank.svg"/>
                    <img src="./assets/photoblank.svg"/>
                    <img src="./assets/photoblank.svg"/>
                </gallery>
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <button class="button small expanded" v-on:click="$refs.gallery.prev()">&lt;</button>
            </div>
            <div class="cell auto">
                <button class="button small expanded" v-on:click="$refs.gallery.next()">&gt;</button>
            </div>
        </div>
        <div class="grid-x">
            {{ detail.description }}
        </div>
        <div class="grid-x">
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="testSwitch" type="checkbox" name="testSwitch">
                    <label class="switch-paddle" for="testSwitch">
                        <span class="show-for-sr">Add to favourites</span>
                    </label>
                </div> 
            </div>
            <div class="cell auto">
                <label for="testSwitch">Add to favourites</label>
            </div>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'detail', null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">
.slide {
    width: 100%;
}
</style>
<script>

import { Siema } from 'vue2-siema';

export default {
    name: 'detailPanel',
    components: {
        gallery: Siema,
    },
    data: function () {
        return {
            
        };
    },
    computed: {
        featureMap: function () {
            return new Map(this.features.map(function (el) {
                return [el.id, el];   
            }));
        }
    },
    props: {
        parkourdexUrl: String,
        features: Array,
        detail: Object,
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
