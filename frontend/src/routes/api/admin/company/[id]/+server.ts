import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { setCookie } from '$lib/setCookie';

export async function PATCH({ request, cookies, params }) {
    const headers = setCookie(cookies)

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/admin/company/${params.id}`, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: headers
    });
    
    return res;
}

export async function DELETE({ cookies, params }) {
    const headers = setCookie(cookies)
    
    const res = await fetcher(`${BACKEND_URL}/admin/company/${params.id}`, {
        method: 'DELETE',
        headers: headers
    });
    
    return res;
}