import axios from 'axios'


export async function suggestProducts(q) {
    const {data: {products}} = await axios.get(`/api/products/suggest/${q}`)
    return products
}

export async function getProduct(productId) {
    const {data: {product}} = await axios.get(`/api/products/${productId}`);
    return product
}

export async function createProduct(productTitle) {
    const {data: {product}} = await axios.post(`/api/products`, {title: productTitle})
    return product
}