<template>
    <div>
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
    props: {
        
    },
    methods: {

    },
    mounted: function () {

    }
}

</script>
