import axios from 'axios'


export async function getMe() {
    const {data: {me}} = await axios.get("/api/me");
    return me
}