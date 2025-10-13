import { writable } from 'svelte/store';

export const dialogStore = writable(0);

type dialogType = 0 | 1;

export function setDialog(type: dialogType) {
    dialogStore.set(type);
}

export function closeDialog() {
    dialogStore.set(0);
}