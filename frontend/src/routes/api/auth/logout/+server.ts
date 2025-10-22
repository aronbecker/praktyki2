import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { setCookie } from '$lib/setCookie';


export async function POST({cookies}) {
    const headers = setCookie(cookies)

    const res = await fetcher(`${BACKEND_URL}/logout`, {
        method: 'POST',
        headers: headers,
        credentials: true
    });
    
    return res;
}
