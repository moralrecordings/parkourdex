<template>
    <div class="grid-container full">
        <h3>Filters</h3>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swShowAll">Show all</label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" id="swShowAll" type="checkbox" name="swShowAll">
                    <label class="switch-paddle" for="swShowAll">
                        <span class="show-for-sr">Show all</span>
                    </label>
                </div> 
            </div>
        </div>
        <div v-for="cat in categories" v-bind:key="cat.id">
            <div class="grid-x" style="border: 1px solid black">
                <div class="cell auto">
                    <label v-bind:for="`swCategory_${ cat.id }`" class="category">{{ cat.name }}</label>
                </div>
                <div class="cell shrink">
                    <div class="switch small">
                        <input class="switch-input" type="checkbox" v-model="cat.enabled" v-bind:id="`swCategory_${ cat.id }`" v-bind:name="`swCategory_${ cat.id }`">
                        <label class="switch-paddle" v-bind:for="`swCategory_${ cat.id }`">
                            <span class="show-for-sr">{{ cat.name }}</span>
                        </label>
                    </div> 
                </div>
            </div>
            <div class="grid-container full">
                <div v-for="feat in cat.features" v-bind:key="feat" class="grid-x" style="border: 1px solid black">
                    <div class="cell auto">
                        <label v-bind:for="`swFeature_${ features[feat].id }`">{{ features[feat].name }}</label>
                    </div>
                    <div class="cell shrink">
                        <div class="switch small">
                            <input class="switch-input" type="checkbox" v-model="features[feat].enabled" v-bind:id="`swFeature_${ features[feat].id }`" v-bind:name="`swFeature_${ features[feat].id }`">
                            <label class="switch-paddle" v-bind:for="`swFeature_${ features[feat].id }`">
                                <span class="show-for-sr">{{ features[feat].name }}</span>
                            </label>
                        </div> 
                    </div>
                </div>
            </div>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', null, null)"><span aria-hidden="true">×</span></button>
    </div>
</template>
<style lang="scss">
.f6inject {
    .off-canvas label.category {
        font-size: 120%;
    }
    
}
</style>
<script>


export default {
    name: 'filterPanel',
    data: function () {
        return {
        };
    },
    props: {
        features: Array,
        categories: Array,
    },
    methods: {
        
    },
    mounted: function () {
    }
}

</script>
