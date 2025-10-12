import type { AddressDto } from "./adresDto";

export type CompanyDto = {
    id: number;
    name: string;
    phoneNumber?: string;
    email?: string;
    website?: string;
    owenerName: string;
    rating: number;
    address: AddressDto;
}
