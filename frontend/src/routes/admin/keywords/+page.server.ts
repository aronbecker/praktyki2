import { BACKEND_URL } from "$lib/backendUrl";
import { fetcher } from "$lib/fetcher";
import { setCookie } from "$lib/setCookie.js";

export async function load({ cookies }) {
    const headers = setCookie(cookies)
    
    const res = await fetcher(`${BACKEND_URL}/admin/categories`, {
        method: 'GET',
        headers: headers,
        credentials: true
    });

    let categories = []

    if (res.ok) {
        const json = await res.json()
        categories = json.categories
    }

    return {
        categories
    }
}