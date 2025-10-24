import pandas as pd
from backend.models.address import Address
from backend.models.company import Company
from backend.models.extensions import db
from .import_keywords import import_slow_kluczowych
from .import_categories import getCattegories

def import_glowny():
    """
    Wczytuje dane firm z pliku Excel i filtruje tylko te, które mają StatusDzialalnosci = 'aktywny'.
    Zwraca DataFrame z wybranymi kolumnami, łącząc Imię i Nazwisko w jedno pole 'NazwaWłaściciela'.
    """
    try:
        df = pd.read_excel('dane_firmy.xlsx')

        if 'StatusDzialalnosci' not in df.columns:
            raise KeyError("Brak kolumny 'StatusDzialalnosci' w pliku Excel.")

        aktywne = df[df['StatusDzialalnosci'].str.lower() == 'aktywny']

        kolumny = [
            'NazwaPodmiotu', 'Telefon', 'Email', 'AdresWWW',
            'Nip', 'Regon', 'Miejscowosc', 'Ulica', 'NrBudynku', 'NrLokalu',
            'Imie', 'Nazwisko', 'GlownyKodPkd', 'PozostaleKodyPkd'
        ]

        brakujace = [k for k in kolumny if k not in aktywne.columns]
        if brakujace:
            raise KeyError(f"Brakujące kolumny w pliku: {', '.join(brakujace)}")


        wynik = aktywne[[
            'NazwaPodmiotu', 'Telefon', 'Email', 'Imie', 'Nazwisko',
            'AdresWWW', 'Nip', 'Regon', 'Miejscowosc', 'Ulica',
            'NrBudynku', 'NrLokalu', 'GlownyKodPkd', 'PozostaleKodyPkd'
        ]]

        for i, row in wynik.iterrows():
            def getVal(propertyName) -> str:
                return row[propertyName] if str(row[propertyName]) != "nan" else ""

            company = Company()
            company.email = getVal("Email")
            company.phone_number = getVal("Telefon")
            company.website_url= getVal("AdresWWW")


            company.nip = getVal("Nip")
            company.regon = getVal("Regon")
            company.name = getVal("NazwaPodmiotu")
            company.owner_name = f"{getVal('Imie')} {getVal('Nazwisko')}"
            company.rating = 0
            company.ratingCount = 0

            address = Address(
                getVal("Miejscowosc"),
                getVal("Ulica"),
                getVal("NrBudynku"),
                getVal("NrLokalu")
            )

            company.address = address
            company.categories = getCattegories(row)

            db.session.add(company)
            db.session.commit()
        
        import_slow_kluczowych()
        
    except FileNotFoundError:
        print(f"❌ Nie znaleziono pliku: {'dane_firmy.xlsx'}")
    except Exception as e:
        print(e.with_traceback())
        print(f"⚠️ Wystąpił błąd: {e}")
