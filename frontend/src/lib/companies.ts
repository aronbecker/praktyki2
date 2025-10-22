import { BACKEND_URL } from "./backendUrl";
import type { CompanyDto } from "./dtos/companyDto";
import { fetcher } from "./fetcher";

export async function getCompanies(page: number, minRating: number = 0): Promise<object> {
    const res = await fetcher(`${BACKEND_URL}/companies?page=${page}&rating=${minRating}`, {
        method: "GET"
    })
    return res.json()
}

export async function getSingleCompany(id: number): Promise<CompanyDto> {
    const res = await fetcher(`${BACKEND_URL}/company/${id}`, {
        method: "GET"
    })
    return res.json()
}

export async function getCompanyComments(companyId: number) {
    const res = await fetcher(`${BACKEND_URL}/company/${companyId}/opinions`, {
        method: "GET"
    })
    return res.json()
}