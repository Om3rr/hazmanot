<template>
    <div class="product--mobile">
            <div class="item--nogrow" @click="addToCart()">
                <font-awesome-icon icon="plus"/>
            </div>
        <div class="item--nogrow" @click="goToShow()">
                <img :src="product.ItemImage">
            </div>
            <div class="item">
            {{ product.ItemName }}
            </div>

            <div class="item--nogrow">
                {{ product.ItemPrice}}
            </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex';

    export default {
        props: ["product"],
        data() {
            return {
                currentAmount: 1
            };
        },
        methods: {
            goToShow() {
                this.$router.push(`/products/${this.product.id}`);
            },
            addToCart() {
                this.addProduct(this.product);
            },
            ...mapActions('products', ['addProduct'])
        }

    };
</script>

<style scoped lang="scss">

</style>