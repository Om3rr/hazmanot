<template>
    <div class="product">
        <div @click="goBack">Back</div>
        {{ product }}
    </div>
</template>

<script>
import { getProduct } from '../../apis/products'

export default {
    name: 'ProductPage',
    data() {
        return {
            product: null,
            loading: true,
        }
    },
    async mounted() {
        const product = await getProduct(this.$route.params.productId)
        this.loading = false
        this.product = product
    },
    computed: {
        productId() {
            return this.$route.params.productId
        },
    },
    methods: {
        goBack() {
            this.$router.go(-1)
        },
    },
}
</script>

<style scoped></style>
