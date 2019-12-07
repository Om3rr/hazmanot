import axios from 'axios'


export async function suggestProducts(q) {
    const {data: {products}} = await axios.get(`/api/products/suggest/${q}`)
    return products
}