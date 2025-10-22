import { getCompanyComments, getSingleCompany } from "$lib/companies";
import { redirect } from "@sveltejs/kit";

export async function load({ params, cookies }) {
    const id = params.id
    if (Number.isInteger(id) || Number.parseInt(id) < 0) {
        throw redirect(300, "/")
    }

    const company = await getSingleCompany(Number(id))
    const comments = await getCompanyComments(Number(id))
    const isAuth = cookies.get("session_id") != undefined

    if (company == undefined) {
        throw redirect(300, "/")
    }

    return { company, comments, isAuth }
}