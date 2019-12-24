<template>
    <div class="bar">
        <div class="title">Hello {{ username }}</div>
        <div class="spacer"></div>
        <div class="badge"><img :src="profilePic"></div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'

    export default {
        computed: {
            ...mapState('user', {username: 'username', profilePic: "profilePic"})
        }
    }
</script>

<style scoped lang="scss">
    .bar {
        display: flex;
        align-items: baseline;
        border-bottom: 1px solid black;
        .title {
            flex: 0 1 auto;
        }
        .spacer {
            flex: auto;
        }
        .badge {
            flex: 0 0 0;
            margin-right: 1em;
            img {
                border-radius: 3em;
                height: 32px;
                width: 32px;
            }

        }
    }
</style>