import type { AddressDto } from "./adresDto";

export type CompanyDto = {
    id: number;
    name: string;
    phone_number?: string;
    email?: string;
    website_url?: string;
    owner_name: string;
    rating: number;
    address: AddressDto;
}
