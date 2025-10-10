class CompanyDto:
    def __init__(self, id: int, name: str, phoneNumber: str, email: str, website: str, ownerName: str, address: any):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.website = website
        self.ownerName = ownerName
        self.address = address