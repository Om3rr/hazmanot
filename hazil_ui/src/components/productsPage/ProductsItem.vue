<template>
    <div class="product">
        <div class="header">
            {{ product.ItemName }}
        </div>
        <div class="body">
            <div class="item">
                 מק״ט: {{ product.ItemCode}}
            </div>
            <div class="image" @click="goToShow()">
                <img :src="product.ItemImage">
            </div>
            <div class="item" @click="addToCart()">
                <div>הוסף לעגלה</div>
            </div>
            <div class="price">
                מחיר: {{ product.ItemPrice}}
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'
    export default {
        props: ["product"],
        data() {
            return {
                currentAmount: 1
            }
        },
        methods: {
           goToShow() {
                this.$router.push(`/products/${this.product.id}`)
            },
            addToCart() {
               this.addProduct(this.product)
            },
            ...mapActions('products', ['addProduct'])
        }

    };
</script>

<style scoped lang="scss">

</style>