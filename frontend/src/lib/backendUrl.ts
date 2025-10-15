// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import { backend_url } from '$env/static/private';

export const BACKEND_URL = getBackendUrl()

function getBackendUrl() {
    if (typeof backend_url !== 'undefined' && backend_url) {
        return backend_url
    } else {
        return "http://127.0.0.1:5000"
    }
}
