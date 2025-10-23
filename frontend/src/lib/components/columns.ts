import type { CompanyDto } from "$lib/dtos/companyDto";
import type { ColumnDef } from "@tanstack/table-core";
 
export const columns: ColumnDef<CompanyDto>[] = [
   {
      accessorKey: "id",
      header: "Id"
   },
   {
      accessorKey: "nip",
      header: "Nip"
   },
   {
      accessorKey: "regon",
      header: "Regon"
   },
   {
      accessorKey: "name",
      header: "Nazwa"
   },
   {
   accessorKey: "email",
   header: "Email",
   },
   {
      accessorKey: "owner_name",
      header: "Właściciel"
   },
   {
      accessorKey: "phone_number",
      header: "Numer telefonu"
   },
   {
      accessorKey: "website_url",
      header: "Strona www"
   },
   {
      accessorKey: "address.town",
      header: "Miejscowość"
   },
   {
      accessorKey: "address.street",
      header: "Ulica"
   },
   {
      accessorKey: "address.buildingNumber",
      header: "Nr. budynku"
   },
   {
      accessorKey: "address.apartmentNumber",
      header: "Nr. lokalu"
   },
];