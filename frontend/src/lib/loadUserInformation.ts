import type { Cookies } from "@sveltejs/kit";
import { BACKEND_URL } from "./backendUrl";
import { fetcher } from "./fetcher";
import type { UserData } from "./stores/userStore";
import { setCookie } from "./setCookie";

export async function loadUserInformation(cookies: Cookies) {
    let userData: UserData | null = null;
    const headers = setCookie(cookies)

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
