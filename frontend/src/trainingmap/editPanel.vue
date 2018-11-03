<template>
<form v-on:submit.prevent="submit">
    <div class="grid-container full">
        <h3 v-if="detail.id == null">Add new spot</h3>
        <h3 v-else>Edit existing spot</h3>
        <div class="grid-x">
            <label class="formControl">Name
                <input type="text" v-model="detail.name" required/>
            </label>
        </div>
        <div class="grid-x">
            <div class="formControl multiselectWrap">Features
                <multiselect v-model="detail.features" v-bind:options="featureOptions" v-bind:multiple="true" 
                             group-values="features" group-label="category" v-bind:group-select="false" 
                             v-bind:searchable="false" v-bind:close-on-select="false" track-by="name" label="name" />
            </div>
        </div>
        <div class="grid-x">
            <label class="formControl">Description
                <textarea v-model="detail.description" required/>
            </label>
        </div>
        <!--div class="grid-x">
            <div class="formControl">Photos
                <uploader :options="{url: '/', paramName: 'file'}">
                    <template slot="clip-uploader-action">
                        <div>
                           <div class="dz-message"><h2> Click or Drag and Drop files here upload </h2></div>
                        </div>
                    </template>

                    <template slot="clip-uploader-body" slot-scope="props">
                        <div v-for="file in props.files">
                            <img v-bind:src="file.dataUrl" />
                            {{ file.name }} {{ file.status }}
                        </div>
                    </template>
                </uploader>
            </div>
        </div-->
        <div class="grid-x expanded button-group">
            <input type="submit" class="button" value="Save"/>
            <button class="button secondary" v-on:click="$emit('toggleMode', 'default')">Cancel</button>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('toggleMode', 'default')"><span aria-hidden="true">×</span></button>
    </div>
</form>
</template>
<style lang="scss">
label.formControl, .formControl.multiselectWrap {
    width: 100%;
}

.f6inject .multiselect {
    margin-bottom: 1rem;
}

label.formControl textarea {
    height: 8em;
}

</style>
<script>
import multiselect from 'vue-multiselect';
//import uploader from 'vue-clip';

import {submitSpot, updateSpot} from './api.js';
import '../multiselect-hack.scss';


export default {
    name: 'detailPanel',
    components: {
        multiselect,
//        uploader,
    },
    data: function () {
        return {};
    },
    computed: {
        featureOptions: function () {
            var vm = this;
            return vm.categories.map(function (el) {
                return {
                    category: el.name,
                    features: el.features.map(function (fl) {
                        return vm.features[fl];
                    })
                };
            });
        }
    },
    props: {
        parkourdexUrl: String,
        categories: Array,
        features: Array,
        detail: Object,
    },
    methods: {
        submit: function () {
            var vm = this;
            var success = function (result) {
                vm.$emit('toggleMode', 'default');
                vm.$emit('updateLocation', result);
            };
            var failure = function (err) {
                vm.$emit('toggleMode', 'default');
                vm.$emit('error', err);
            };
            if (vm.detail.id == null) {
                submitSpot(vm.parkourdexUrl, vm.detail, success, failure); 
            } else {
                updateSpot(vm.parkourdexUrl, vm.detail, vm.detail.id, success, failure);
            }
        },
    },
    mounted: function () {

    }
}

</script>
