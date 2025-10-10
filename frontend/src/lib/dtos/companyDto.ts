import type { AddressDto } from "./adresDto";

export type CompanyDto = {
    id: string;
    name: string;
    phoneNumber?: string;
    email?: string;
    website?: string;
    owenerName: string;
    address: AddressDto;
}
