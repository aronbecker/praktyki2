# \# 🚀 SkokiFirmy

# 

# \## 🎯 Cel Projektu

# 

# Projekt \*\*SkokiFirmy\*\* został stworzony, aby \*\*ułatwić mieszkańcom Gminy Skoki znajdowanie dobrych i sprawdzonych fachowców oraz lokalnych firm\*\*. Platforma ma służyć jako wiarygodne źródło kontaktów i rekomendacji.

# 

# ---

# 

# \## 📅 Informacje o Projekcie

# 

# | Wskaźnik | Wartość |

# | :--- | :--- |

# | \*\*Zakres\*\* | Gmina Skoki |

# | \*\*Status\*\* | W trakcie rozwoju (Development) |

# | \*\*Szacowany Czas Wykonania\*\* | 1 miesiąc |

# 

# ---

# 

# \## 🧑‍💻 Autorzy

# 

# Projekt został zrealizowany przez zespół w składzie:

# 

# \* \*\*Aron Becker\*\*

# \* \*\*Błażej Kubicki\*\*

# \* \*\*Dawid Kruczek\*\*

# 

# ---

# 

# \## ⚙️ Uruchomienie Lokalnie (Dla Deweloperów)

## Frontend
`cd frontend` - przejście do folderu

`npm i` - zainstalowanie zależności

`npm run dev` - uruchomienie aplikacji

## Backend
`cd backend` - przejście do folderu

`pip install -r requirements.txt` - zainstalowanie zależności

Uruchomić lokalną baze danych mysql

Stwórz plik `.env` ze zmienną `db_URI`, która powinna być ustawiona na adres bazy danych mysql (dla dewelopmentu lokalna)

`flask db init` - inicjuje lokalnie moduł bazodanowy (użyć tylko raz) 

`flask db migrate -m "Initial migration."` - tworzy migracje, (używać jej zawsze gdy zmienia się strukturę bazy danych)

`flask db upgrade` - komenda zapisująca zmiany w bazie danych (używać po użyciu komendy `migrate`)

`cd ..` - cofniecie się folder do tyłu

`py -m backend.app` - uruchamia serwer 

# \### Wymagania wstępne

# 

# 

# \### Instrukcja

# 

# 

