<template>
    <div>
        Spinner...
    </div>
</template>

<script>
    import {mapState} from 'vuex';
    export default {
        props: ["toPath", "failPath"],
        computed: {
            ...mapState('user', ['loading', 'loggedIn'])
        },
        watch: {
            loading() {
                if(this.loading) {
                    return
                }
                this.loggedIn ? this.$router.push({path: this.$route.query.redirect, query: this.$route.query.query}) : this.$router.push({path: "/user/login"});
            }
        },

    }
</script>

<style scoped>

</style>