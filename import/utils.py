# utils.py
# -*- coding: utf-8 -*-


def getCategoryFromPkd(pkdCode: str) -> str:
    """
    Zwraca kategorię (string) odpowiednią do kodu PKD.
    """
    try:
        code = int(pkdCode[0]+pkdCode[1]) 
    except ValueError:
        return ""

    for codes, category in PKD_TO_CATEGORY.items():
        if code in codes:
            return category

    return ""


def getKeywordFromCategory(category: str) -> list:
    """
    Zwraca listę słów kluczowych (lista stringów) dla podanej kategorii.
    """
    return CATEGORY_TO_KEYWORDS.get(category.upper(), ["brak danych"])


PKD_TO_CATEGORY = {
    (1, 2, 3): "ROLNICTWO, LEŚNICTWO I RYBACTWO",
    (5, 6, 7, 8, 9): "GÓRNICTWO I WYDOBYWANIE",
    tuple(range(10, 34)): "PRZETWÓRSTWO PRZEMYSŁOWE",
    (35,): "ZAOPATRZENIE ENERGETYCZNE OBIEKTÓW",
    (36, 37, 38, 39): "USŁUGI KOMUNALNE I REKULTYWACJA",
    (41, 42, 43): "BUDOWNICTWO",
    (46, 47): "HANDEL",
    (49, 50, 51, 52, 53): "TRANSPORT I LOGISTYKA",
    (55, 56): "ZAKWATEROWANIE I GASTRONOMIA",
    (58, 59, 60): "DZIAŁALNOŚĆ MEDIALNO-WYDAWNICZA",
    (61, 62, 63): "USŁUGI IT I TELEKOMUNIKACJA",
    (64, 65, 66): "FINANSE I UBEZPIECZENIA",
    (68,): "USŁUGI NIERUCHOMOŚCIOWE",
    (69, 70, 71, 72, 73, 74, 75): "USŁUGI NAUKOWE I TECHNICZNE",
    (77, 78, 79, 80, 81, 82): "USŁUGI ADMINISTRACYJNE",
    (84,): "ADMINISTRACJA I OBRONA",
    (85,): "EDUKACJA",
    (86, 87, 88): "ZDROWIE I POMOC",
    (90, 91, 92, 93): "KULTURA I REKREACJA",
    (94, 95, 96): "USŁUGI RÓŻNE",
    (97, 98): "GOSPODARSTWA DOMOWE",
    (99,): "ORGANIZACJE EKSTERYTORIALNE",
}

CATEGORY_TO_KEYWORDS = {
    "ROLNICTWO, LEŚNICTWO I RYBACTWO": ["uprawa", "hodowla", "rybołówstwo"],
    "GÓRNICTWO I WYDOBYWANIE": ["kopalnia", "węgiel", "surowce"],
    "PRZETWÓRSTWO PRZEMYSŁOWE": ["produkcja", "fabryka", "przetwórstwo"],
    "ZAOPATRZENIE ENERGETYCZNE OBIEKTÓW": ["energia", "elektryczność", "ogrzewanie"],
    "USŁUGI KOMUNALNE I REKULTYWACJA": ["śmieci", "oczyszczanie", "recykling"],
    "BUDOWNICTWO": ["budowa", "konstrukcja", "architektura"],
    "HANDEL": ["sprzedaż", "sklep", "hurtownia"],
    "TRANSPORT I LOGISTYKA": ["przewóz", "magazyn", "spedycja"],
    "ZAKWATEROWANIE I GASTRONOMIA": ["hotel", "restauracja", "nocleg"],
    "DZIAŁALNOŚĆ MEDIALNO-WYDAWNICZA": ["prasa", "media", "publikacja"],
    "USŁUGI IT I TELEKOMUNIKACJA": ["oprogramowanie", "sieci", "technologie"],
    "FINANSE I UBEZPIECZENIA": ["bank", "inwestycje", "polisa"],
    "USŁUGI NIERUCHOMOŚCIOWE": ["wynajem", "sprzedaż", "nieruchomości"],
    "USŁUGI NAUKOWE I TECHNICZNE": ["badania", "doradztwo", "eksperyment"],
    "USŁUGI ADMINISTRACYJNE": ["biuro", "dokumenty", "obsługa"],
    "ADMINISTRACJA I OBRONA": ["rząd", "wojsko", "bezpieczeństwo"],
    "EDUKACJA": ["szkoła", "nauka", "kurs"],
    "ZDROWIE I POMOC": ["szpital", "lekarz", "opieka"],
    "KULTURA I REKREACJA": ["teatr", "sport", "rozrywka"],
    "USŁUGI RÓŻNE": ["fryzjer", "sprzątanie", "serwis"],
    "GOSPODARSTWA DOMOWE": ["gospodarstwo", "dom", "rodzina"],
    "ORGANIZACJE EKSTERYTORIALNE": ["ambasada", "konsulat", "organizacja"],
}
