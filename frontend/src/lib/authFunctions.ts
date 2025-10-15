import type { RegistrationDto } from "./dtos/registrationDto";
import type { LoginDto } from "./dtos/loginDto";
import { fetcher } from "./fetcher";
import { userStore } from "./stores/userStore";
import { toast } from "svelte-sonner";

export async function Login(loginDto: LoginDto) {
    const response = await fetcher("/api/auth/login", {
        method: "POST",
        body: JSON.stringify(loginDto),
    })

    return response;
}


export async function Register(loginDto: RegistrationDto) {
    const response = await fetcher("/api/auth/register", {
        method: "POST",
        body: JSON.stringify(loginDto),
    })

    return response;
}

export async function Logout() {
    const response = await fetcher("/api/auth/logout", {
        method: "POST"
    })
    if (response.ok) {
        userStore.update(() => null)
        toast.success("Wylogowano z konta")
    }
}