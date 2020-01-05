<template>
    <div>
        Login
        <GoogleLoginButton @loggedIn="loggedIn" />
    </div>
</template>

<script>
import GoogleLoginButton from './GoogleLoginButton'
import { mapActions } from 'vuex'
export default {
    components: { GoogleLoginButton },
    methods: {
        ...mapActions('user', ['initUser']),
        async loggedIn() {
            await this.initUser()
            this.$router.push({ path: '/' })
        },
    },
}
</script>

<style scoped></style>
