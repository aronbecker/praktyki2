import { writable } from 'svelte/store';

export const dialogStore = writable<DialogType>({
    code:0,
    data: {}
});

type DialogType = {
    code: 0 | 1 | 2,
    data?: object
};

export function setDialog(type: DialogType) {
    dialogStore.set(type);
}
