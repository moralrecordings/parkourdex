<template>
    <div class="grid-container full">
        <h3>Add new spot</h3>
        <div class="grid-x">
            <label class="formControl">Name
                <input type="text"/>
            </label>
        </div>
        <div class="grid-x">
            <div class="formControl multiselectWrap">Features
                <multiselect v-model="featureSelect" v-bind:options="featureOptions" v-bind:multiple="true" group-values="features" group-label="category" v-bind:group-select="false" v-bind:searchable="false" v-bind:close-on-select="false" track-by="name" label="name" />
            </div>
        </div>
        <div class="grid-x">
            <label class="formControl">Description
                <textarea />
            </label>
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

label.formControl textarea {
    height: 8em;
}

</style>
<script>
import multiselect from 'vue-multiselect';
import '../multiselect-hack.scss';


export default {
    name: 'detailPanel',
    components: {
        multiselect
    },
    data: function () {
        return {
            featureSelect: []
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
