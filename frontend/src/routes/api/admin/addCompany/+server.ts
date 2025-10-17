import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';

export async function POST({ request, cookies }) {
    const sessionId = cookies.get("session_id")

    if (sessionId == undefined) {
        return new Response()
    }

    const headers = new Headers();
    headers.append('cookie', `session_id=${sessionId}`);

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/admin/addCompany`, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: true,
        headers: headers
    });
    
    return res;
}
