<template>
    <div v-if="detail" class="grid-container full">
        <h3>{{ detail.name }}</h3>
        <div class="grid-x">
            <template v-for="feature in detail.features">
                <img v-if="featureMap.get(feature) && featureMap.get(feature).icon" v-bind:src="`${parkourdexUrl}${featureMap.get(feature).icon}`" v-bind:title="featureMap.get(feature).name" />
            </template>
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

</style>
<script>

export default {
    name: 'detailPanel',
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
