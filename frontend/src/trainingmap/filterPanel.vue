<template>
    <div class="grid-container full">
        <h3>Legend</h3>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swMyLocation">
                    <img src="./assets/gps.svg"/> My location
                </label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swMyLocation" name="swMyLocation" v-model="options.showMyLocation" v-on:change="$emit('updateFilters', 'options', 'showMyLocation', options.showMyLocation)">
                    <label class="switch-paddle" for="swMyLocation">
                        <span class="show-for-sr">My location</span>
                    </label>
                </div> 
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swSpots">
                    <img src="./assets/pin.svg"/> Training spot
                </label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swSpots" name="swSpots" v-model="options.showSpots" v-on:change="$emit('updateFilters', 'options', 'showSpots', options.showSpots)">
                    <label class="switch-paddle" for="swSpots">
                        <span class="show-for-sr">Training spot</span>
                    </label>
                </div> 
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swVisitedSpots">
                    <img src="./assets/visit.svg"/> Visited training spot
                </label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swVisitedSpots" name="swVisitedSpots" v-model="options.showVisitedSpots" v-on:change="$emit('updateFilters', 'options', 'showVisitedSpots', options.showVisitedSpots)">
                    <label class="switch-paddle" for="swVisitedSpots">
                        <span class="show-for-sr">Visited training spot</span>
                    </label>
                </div> 
            </div>
        </div>
 
        <div class="grid-x">
            <div class="cell auto">
                <label for="swFavourites">
                    <img src="./assets/fav.svg"/> Favourites
                </label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swFavourites" name="swFavourites" v-model="options.showFavourites" v-on:change="$emit('updateFilters', 'options', 'showFavourites', options.showFavourites)">
                    <label class="switch-paddle" for="swFavourites">
                        <span class="show-for-sr">Favourites</span>
                    </label>
                </div> 
            </div>
        </div>

        <div class="grid-x">
            <div class="cell auto">
                <label for="swShortlist">
                    <img src="./assets/short.svg"/> Shortlist
                </label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swShortlist" name="swShortlist" v-model="options.showShortlist" v-on:change="$emit('updateFilters', 'options', 'showShortlist', options.showShortlist)">
                    <label class="switch-paddle" for="swShortlist">
                        <span class="show-for-sr">Shortlist</span>
                    </label>
                </div> 
            </div>
        </div>



        <h3>Features</h3>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swShowAll" class="category">Show all</label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swShowAll" name="swShowAll" v-model="options.showAll" v-on:change="$emit('updateFilters', 'options', 'showAll', options.showAll)">
                    <label class="switch-paddle" for="swShowAll">
                        <span class="show-for-sr">Show all</span>
                    </label>
                </div> 
            </div>
        </div>
        <div v-for="(cat, catIndex) in categories" v-bind:key="cat.id">
            <div class="grid-x">
                <div class="cell auto">
                    <label v-bind:for="`swCategory_${ cat.id }`" class="category">{{ cat.name }}</label>
                </div>
                <div class="cell shrink">
                    <div class="switch small">
                        <input class="switch-input" type="checkbox" v-bind:id="`swCategory_${ cat.id }`" v-bind:name="`swCategory_${ cat.id }`" v-model="cat.enabled" v-on:change="$emit('updateFilters', 'category', catIndex, cat.enabled)">
                        <label class="switch-paddle" v-bind:for="`swCategory_${ cat.id }`">
                            <span class="show-for-sr">{{ cat.name }}</span>
                        </label>
                    </div> 
                </div>
            </div>
            <div class="grid-container full">
                <div v-for="feat in cat.features" v-bind:key="feat" class="grid-x">
                    <div class="cell auto">
                        <label v-bind:for="`swFeature_${ features[feat].id }`">{{ features[feat].name }}</label>
                    </div>
                    <div class="cell shrink">
                        <div class="switch small">
                            <input class="switch-input" type="checkbox" v-bind:id="`swFeature_${ features[feat].id }`" v-bind:name="`swFeature_${ features[feat].id }`" v-model="features[feat].enabled" v-on:change="$emit('updateFilters', 'feature', feat, features[feat].enabled)">
                            <label class="switch-paddle" v-bind:for="`swFeature_${ features[feat].id }`">
                                <span class="show-for-sr">{{ features[feat].name }}</span>
                            </label>
                        </div> 
                    </div>
                </div>
            </div>
        </div>
        <div class="grid-x">
            <div class="cell auto">
                <label for="swUntagged" class="category">Untagged</label>
            </div>
            <div class="cell shrink">
                <div class="switch small">
                    <input class="switch-input" type="checkbox" id="swUntagged" name="swUntagged" v-model="options.showUntagged" v-on:change="$emit('updateFilters', 'options', 'showUntagged', options.showUntagged)">
                    <label class="switch-paddle" for="swUntagged">
                        <span class="show-for-sr">Untagged</span>
                    </label>
                </div> 
            </div>
        </div>
        <button class="close-button" type="button" v-on:click="$emit('showPanel', 'filters', null)"><span aria-hidden="true">×</span></button>
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
        options: Object,
    },
    methods: {
        
    },
    mounted: function () {
    }
}

</script>
