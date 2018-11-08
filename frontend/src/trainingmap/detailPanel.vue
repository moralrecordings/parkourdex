<template>
    <div v-if="detail" class="grid-container full">
        <h3>{{ detail.name }}</h3>
        <div class="grid-x">
            <ul>
                <li v-for="feature in detail.features" v-bind:key="feature" v-if="featureMap.get(feature)" >
                    <img v-if="featureMap.get(feature).icon" v-bind:src="`${parkourdexUrl}${featureMap.get(feature).icon}`" v-bind:title="featureMap.get(feature).name" /> {{ featureMap.get(feature).name }}
                </li>
            </ul>
        </div>
        <div class="grid-x">
            <div class="cell auto" v-if="detail.photos.length > 0">
                <gallery ref="gallery" v-bind:options="{loop: true}">
                    <img v-for="img in detail.photos" v-bind:key="img" v-bind:src="img"/>
                </gallery>
            </div>
        </div>
        <div class="grid-x" v-if="detail.photos.length > 1">
            <div class="cell auto">
                <button class="button small expanded" v-on:click="$refs.gallery.prev()">&lt;</button>
            </div>
            <div class="cell auto">
                <button class="button small expanded" v-on:click="$refs.gallery.next()">&gt;</button>
            </div>
        </div>
        <div class="grid-x expanded button-group">
            <button class="button">Add photo</button>
            <button class="button" v-if="detail.editable" v-on:click="toggleEdit">Edit spot</button>
        </div>
        <div class="grid-x">
            {{ detail.description }}
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <label for="favourite"><img src="./assets/fav.svg"> Add to favourites</label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="favourite" type="checkbox" name="testSwitch">
                    <label class="switch-paddle" for="favourite">
                        <span class="show-for-sr">Favourite</span>
                    </label>
                </div> 
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <label for="shortlist"><img src="./assets/short.svg"> Add to shortlist</label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="shortlist" type="checkbox" name="testSwitch">
                    <label class="switch-paddle" for="shortlist">
                        <span class="show-for-sr">Shortlist</span>
                    </label>
                </div> 
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <hr/>
            </div>
        </div>
        <div class="grid-x">
            <h5>Training lore</h5>
        </div>
        <div>
            <div class="grid-x">
                <div class="cell auto">
                    <textarea rows="5" placeholder="Add your own lore here..."/>
                </div>
            </div>
            <div class="grid-x">
                <button class="button expanded">Submit lore</button>
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
        toggleEdit: function () {
            var vm = this;
            vm.$emit('toggleEdit', vm.detail);
        },

    },
    mounted: function () {

    }
}

</script>
