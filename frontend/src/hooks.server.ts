import { loadUserInformation } from '$lib/loadUserInformation';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
    if (event.url.pathname.startsWith('/error')) {
		return resolve(event);
	}

    const userInfo = await loadUserInformation(event.cookies)
    event.locals.user = userInfo.userData ?? undefined
    
	if (event.url.pathname.startsWith('/admin')) {
        if (!userInfo.userData || userInfo.userData.role !== 'admin') {
            return new Response(null, {
                status: 307,
                headers: { location: '/' }
            })
        }
	}

	const response = await resolve(event);
	return response;
};