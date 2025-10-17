import { getCompanies } from "$lib/companies";

export async function load() {
    const page = await getCompanies(0)

	return { page }
}