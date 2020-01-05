<template>
    <div class="search-bar-container">
        <input
            class="search-bar"
            placeholder="חיפוש"
            :value="search"
            v-on:input="onInput"
            type="text"
        />
    </div>
</template>

<script>
import _ from 'lodash'

export default {
    props: ['search'],
    methods: {
        emitInput($event) {
            this.$emit('input', $event.target.value)
        },
        onInput: _.debounce(function(e) {
            this.emitInput(e)
        }, 500),
    },
}
</script>

<style scoped lang="scss">
.search-bar-container {
    text-align: center;
}
.search-bar {
    font-size: 18px;
    padding: 0.3em;
    direction: rtl;
    margin: 0.5em;
    width: 20em;
}
</style>
