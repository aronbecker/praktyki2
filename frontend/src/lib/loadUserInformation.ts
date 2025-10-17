import type { Cookies } from "@sveltejs/kit";
import { BACKEND_URL } from "./backendUrl";
import { fetcher } from "./fetcher";
import type { UserData } from "./stores/userStore";

export async function loadUserInformation(cookies: Cookies) {
    let userData: UserData | null = null;
    const sessionId = cookies.get("session_id");

    if (sessionId == undefined) {
        return {
            userData: null,
        };
    }

    const headers = new Headers();
    headers.append("cookie", `session_id=${sessionId}`);

    const res = await fetcher(`${BACKEND_URL}/me`, {
        method: "GET",
        headers: headers,
        credentials: true,
    });
    if (res.status === 200) {
        userData = await res.json();
    }

    return {
        userData: userData,
    };
}
