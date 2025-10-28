import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { setCookie } from '$lib/setCookie.js';

export async function PATCH({ request, cookies, params }) {
    const headers = setCookie(cookies)
    const categoryId = params.id

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/admin/categories/${categoryId}`, {
        method: 'PATCH',
        body: JSON.stringify(data),
        credentials: true,
        headers: headers
    });
    
    return res;
}

