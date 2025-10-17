// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { env } from '$env/dynamic/public';

export const BACKEND_URL = env.PUBLIC_BACKEND_URL ?? 'http://127.0.0.1:5000';
