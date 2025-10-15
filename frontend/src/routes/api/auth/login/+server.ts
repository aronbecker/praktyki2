import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';

export async function POST({ request }) {
    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/login`, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: true
    });
    
    return res;
}
