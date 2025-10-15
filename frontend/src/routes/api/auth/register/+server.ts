import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher.js';
import { json } from '@sveltejs/kit';

export async function POST({ request, fetch }) {
    const data = await request.json()

    const res = await fetcher(`${BACKEND_URL}/register`, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: true
    });

    if (!res.ok) {
        return res
    }

    const loginFetch = await fetch("/api/auth/login", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json;charset=UTF-8"
        },
        credentials: "include"
    })
    
    const loginResult = await loginFetch.json();

    return json(loginResult, { status: loginFetch.status });
}
