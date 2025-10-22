import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';

export async function PATCH({ request, cookies, params }) {
    const sessionId = cookies.get("session_id")

    if (sessionId == undefined) {
        return new Response()
    }

    const headers = new Headers();
    headers.append('cookie', `session_id=${sessionId}`);

    const data = await request.json()
    const res = await fetcher(`${BACKEND_URL}/admin/company/${params.id}`, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: headers
    });
    
    return res;
}

export async function DELETE({ cookies, params }) {
    const sessionId = cookies.get("session_id")


    if (sessionId == undefined) {
        return new Response()
    }

    const headers = new Headers();
    headers.append('cookie', `session_id=${sessionId}`);

    const res = await fetcher(`${BACKEND_URL}/admin/company/${params.id}`, {
        method: 'DELETE',
        headers: headers
    });
    
    return res;
}