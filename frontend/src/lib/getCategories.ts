import { BACKEND_URL } from "./backendUrl";
import { fetcher } from "./fetcher";

export async function getCategories() {
    const res = await fetcher(`${BACKEND_URL}/categories`, {
        method: "GET"
    })
    return await res.json()
}