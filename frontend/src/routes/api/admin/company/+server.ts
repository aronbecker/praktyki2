import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { setCookie } from '$lib/setCookie.js';

export async function POST({ request, cookies }) {
    const headers = setCookie(cookies)

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/admin/addCompany`, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: true,
        headers: headers
    });
    
    return res;
}

