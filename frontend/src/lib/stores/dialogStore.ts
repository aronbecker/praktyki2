import { writable } from 'svelte/store';

export const dialogStore = writable(0);

type DialogType = 0 | 1;

export function setDialog(type: DialogType) {
    dialogStore.set(type);
}

export function closeDialog() {
    dialogStore.set(0);
}