import type { Cookies } from "@sveltejs/kit";

export function setCookie(cookies: Cookies): Headers {
    const sessionId = cookies.get("session_id")
    const headers = new Headers();

    if (sessionId != undefined) {
        headers.append('cookie', `session_id=${sessionId}`);
    }

    return headers
}