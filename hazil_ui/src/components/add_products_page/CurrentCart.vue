<template>
    <div>
        <div v-for="prod in cart" :key="prod.ItemCode" @click="deleteProduct(prod)">
            {{prod.ItemName}} - {{prod.amount}}
        </div>
        --------
        totalPrice - {{totalPrice}}
    </div>
</template>

<script>
    import {mapState, mapActions, mapGetters} from 'vuex'
    export default {
        name: "CurrentCart",
        computed: {
            ...mapState('products', {cart: 'products'}),
            ...mapGetters('products', ['totalPrice'])
        },
        methods: {
            ...mapActions('products', ['deleteProduct'])
        }
    }
</script>

<style scoped>

</style>