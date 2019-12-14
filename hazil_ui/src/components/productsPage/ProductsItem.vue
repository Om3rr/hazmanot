<template>
    <div class="products--line">
            <div class="products--line--item--small">{{product.ItemName}}</div>
            <div class="products--line--item">מק"ט</div>
            <div class="products--line--item">תיאור מוצר</div>
            <div class="products--line--item">
                <button @click="currentAmount = parseInt(currentAmount) + 1">
                    +
                </button>
                <input v-model="currentAmount" type="number" min="1">
                <button :disabled="currentAmount === 1" @click="currentAmount = parseInt(currentAmount) - 1">
                    -
                </button>
            </div>
            <div class="products--line--item">הוסף</div>
        </div>
</template>

<script>
    export default {
        props: ["product"],
        data() {
            return {
                currentAmount: 1
            }
        }
    };
</script>

<style scoped>

</style>