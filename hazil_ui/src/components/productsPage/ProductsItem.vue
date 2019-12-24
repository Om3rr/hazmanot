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
                <img src="https://res.cloudinary.com/shufersal/image/upload/f_auto,q_auto/v1551800918/prod/product_images/products_medium/BNV56_M_P_7290015765626_1.png">
            </div>
            <div class="item">
                <div>הוסף לעגלה</div>
            </div>
            <div class="price">
                מחיר: {{ product.ItemPrice}}
            </div>
        </div>
    </div>
</template>

<script>
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
            }
        }

    };
</script>

<style scoped lang="scss">

</style>