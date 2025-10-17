import { writable } from 'svelte/store';

export const userStore = writable<UserData | null>(null);

export type UserData = {
    email: string
    firstname: string
    lastname: string
    role: 'user' | 'admin'
}
