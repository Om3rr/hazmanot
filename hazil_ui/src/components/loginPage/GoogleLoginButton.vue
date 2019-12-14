<template>
    <button @click="login">Login!</button>
</template>

<script>
    import {tokenLogin} from "../../apis/orders";

    export default {
        data() {
            return {
                token: ''
            }
        },
        methods: {
            login() {
                this.$gAuth.signIn()
                    .then(this.onSuccess)
                    .catch(this.onError);
            },
            async onSuccess(gUser) {
                this.token = gUser.getAuthResponse().id_token;
                await tokenLogin(this.token);
                this.$emit('loggedIn')
            },
            onError(error) {
                console.log(error);
            }
        }
    };
</script>

<style>
    .google-signin-button {
        color: white;
        background-color: red;
        height: 50px;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px 25px 20px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
</style>