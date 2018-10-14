<template>
    <div class="grid-container full">
        <h3 v-if="target.id == null">Add new spot</h3>
        <h3 v-else>Edit existing spot</h3>
        <div class="grid-x">
            <label class="formControl">Name
                <input type="text" v-model="target.name"/>
            </label>
        </div>
        <div class="grid-x">
            <div class="formControl multiselectWrap">Features
                <multiselect v-model="target.features" v-bind:options="featureOptions" v-bind:multiple="true" 
                             group-values="features" group-label="category" v-bind:group-select="false" 
                             v-bind:searchable="false" v-bind:close-on-select="false" track-by="name" label="name" />
            </div>
        </div>
        <div class="grid-x">
            <label class="formControl" v-model="target.description">Description
                <textarea v-model="target.description"/>
            </label>
        </div>
        <div class="grid-x">
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
        </div>
        <div class="grid-x expanded button-group">
            <button class="button">Save</button>
            <button class="button secondary" v-on:click="$emit('toggleMode', 'default')">Cancel</button>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('toggleMode', 'default')"><span aria-hidden="true">×</span></button>
    </div>
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
import uploader from 'vue-clip';
import '../multiselect-hack.scss';


export default {
    name: 'detailPanel',
    components: {
        multiselect,
        uploader
    },
    data: function () {
        return {
            target: {
                id: null,
                name: '',
                description: '',
                features: []
            },
        };
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
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
