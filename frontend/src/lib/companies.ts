import { BACKEND_URL } from "./backendUrl";
import { fetcher } from "./fetcher";

export async function getCompanies(page: number): Promise<object> {
    const res = await fetcher(`${BACKEND_URL}/companies?page=${page}`, {
        method: "GET"
    })
    return res.json()
}
