import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { setCookie } from '$lib/setCookie';
import { error } from '@sveltejs/kit';

export async function POST({ request, cookies, url }) {
    const headers = setCookie(cookies)
    const companyId = url.searchParams.get('companyId')

    if (companyId == null || isNaN(companyId) || Number(companyId) <= 0) {
        error(400)
    }

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/company/${Number(companyId)}/comments`, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: true,
        headers: headers
    });
    
    return res;
}

