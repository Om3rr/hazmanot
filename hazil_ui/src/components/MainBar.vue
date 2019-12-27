<template>
    <div class="bar">
        <div class="title">Hello {{ username }}</div>
        <div class="spacer"></div>
        <div class="badge" @click="goToCart()"><font-awesome-icon icon="shopping-cart" /></div>
        <div class="badge"><img :src="profilePic"></div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'

    export default {
        computed: {
            ...mapState('user', {username: 'username', profilePic: "profilePic"}),
        },
        methods: {
            goToCart() {
                this.onCart() ? this.$router.push('/') : this.$router.push("/cart")
            },
            onCart() {
                const {currentRoute: {fullPath}} = this.$router;
                return fullPath === '/cart'
            }
        },

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
            svg {
                height: 24px;
                width: 24px;
            }

        }
    }
</style>