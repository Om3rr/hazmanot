import axios from 'axios'


export async function getMe() {
    const {data: {me}} = await axios.get("/api/me");
    return me
}

export async function tokenLogin(token) {
    const {data} = await axios.post("/api/auth/token", {token});
    return data;
}