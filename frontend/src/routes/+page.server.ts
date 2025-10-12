import type { CompanyDto } from "$lib/dtos/companyDto";

// TODO: Ładowanie z serwera

export function load() {
	const companies: CompanyDto[] = [
        {
            id: 1,
            name: "Budowlanka Maniek",
            phoneNumber: "924 045 231",
            email: "mailbudowa@gmail.com",
            website: "www.ManiekBudowa.pl",
            owenerName: "Maniek Byczek",
            rating: 4.5,
            address: {
                town: "Skoki",
                street: "Parkowa",
                buildingNumber: "4",
                apartmentNumber: "2"
            }
        },
        {
            id: 1,
            name: "Budowlanka Maniek",
            phoneNumber: "924 045 231",
            website: "www.ManiekBudowa.pl",
            owenerName: "Maniek Byczek",
            rating: 1,
            address: {
                town: "Skoki",
                street: "Parkowa",
                buildingNumber: "4",
                apartmentNumber: "2"
            }
        },
        {
            id: 1,
            name: "Budowlanka Maniek",
            phoneNumber: "924 045 231",
            email: "mailbudowa@gmail.com",
            owenerName: "Maniek Byczek",
            rating: 2.3,
            address: {
                town: "Skoki",
                street: "Parkowa",
                buildingNumber: "4",
                apartmentNumber: "2"
            }
        },
        {
            id: 1,
            name: "Budowlanka Maniek",
            email: "mailbudowa@gmail.com",
            owenerName: "Maniek Byczek",
            rating: 3.7,
            address: {
                town: "Skoki",
                street: "Parkowa",
                buildingNumber: "4",
                apartmentNumber: ""
            }
        },
    ]

    for (let i = 0; i < 2; i++) {
        companies.push(...companies);
    }

	return {
		companies
	};
}