<template>
    <div class="grid-container full">
        <h3>Filters</h3>
        <div class="grid-x">
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="swShowAll" type="checkbox" name="swShowAll">
                    <label class="switch-paddle" for="swShowAll">
                        <span class="show-for-sr">Show all</span>
                    </label>
                </div> 
            </div>
            <div class="cell auto">
                <label for="swShowAll">Show all</label>
            </div>
        </div>
        <div class="grid-x" style="border: 1px solid black">
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="swShowGrp" type="checkbox" name="swShowGrp">
                    <label class="switch-paddle" for="swShowGrp">
                        <span class="show-for-sr">Show grp</span>
                    </label>
                </div> 
            </div>
            <div class="cell auto">
                <label for="swShowGrp">Show grp</label>
            </div>
        </div>
        <div class="grid-container full">
            <div class="grid-x" style="border: 1px solid black">
                <div class="cell shrink">
                    <div class="switch small">
                        <input class="switch-input" id="swShowFeat1" type="checkbox" name="swShowFeat1">
                        <label class="switch-paddle" for="swShowFeat1">
                            <span class="show-for-sr">Show feat1</span>
                        </label>
                    </div> 
                </div>
                <div class="cell auto">
                    <label for="swShowFeat1">Show feat1</label>
                </div>
            </div>
            <div class="grid-x" style="border: 1px solid black">
                <div class="cell shrink">
                    <div class="switch small">
                        <input class="switch-input" id="swShowFeat2" type="checkbox" name="swShowFeat2">
                        <label class="switch-paddle" for="swShowFeat2">
                            <span class="show-for-sr">Show feat2</span>
                        </label>
                    </div> 
                </div>
                <div class="cell auto">
                    <label for="swShowFeat2">Show feat2</label>
                </div>
            </div>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', null, null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">

</style>
<script>


export default {
    name: 'filterPanel',
    data: function () {
        return {
        };
    },
    props: {
        categories: Array,
    },
    methods: {
        
    },
    mounted: function () {
    }
}

</script>
