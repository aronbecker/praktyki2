import { error } from '@sveltejs/kit';

export const load = ({ url }) => {
	const status = Number(url.searchParams.get('status') ?? 500);
	throw error(status);
};