import { BACKEND_URL } from '$lib/backendUrl';
import { fetcher } from '$lib/fetcher';
import type { UserData } from '$lib/stores/userStore';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({cookies}) => {
    let userData: UserData | null = null
    const sessionId = cookies.get("session_id")

    if (sessionId == undefined) {
        return {
            userData: null
        }
    }

    const headers = new Headers();
    headers.append('cookie', `session_id=${sessionId}`);

	const res = await fetcher(`${BACKEND_URL}/me`, {
        method: "GET",
        headers: headers,
        credentials: true
    })
    if (res.status === 200) {
        userData = await res.json()
    }

    return {
		userData: userData
	};
};