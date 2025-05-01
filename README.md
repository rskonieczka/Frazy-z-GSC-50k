# Pobieranie słów kluczowych z Google Search Console (GSC)

## Opis
Skrypt w pytonie `keywords-gsc.py` automatycznie pobiera wszystkie słowa kluczowe (frazy) z Google Search Console dla wybranej domeny w zakresie od dnia dzisiejszego do 16 miesięcy wstecz i eksportuje wynik do pliku CSV.

## Wymagania
- Python 3
- Pakiety: `pandas`, `google-api-python-client`, `oauth2client`
- Plik autoryzacyjny: `indexing-api.json` (Service Account z dostępem do GSC)

## Przygotowanie środowiska
1. Umieść plik `indexing-api.json` w katalogu skryptu.
2. Zainstaluj wymagane pakiety:
   ```bash
   pip install -r requirements.txt
   ```

## Jak uzyskać plik indexing-api.json (Service Account)

Aby pobrać dane z Google Search Console przez API, potrzebujesz pliku autoryzacyjnego konta serwisowego (`indexing-api.json`).

### Krok po kroku:
1. **Wejdź do Google Cloud Console:**
   https://console.cloud.google.com/
2. **Utwórz nowy projekt** (lub wybierz istniejący).
3. **Włącz Search Console API**:
   - W menu po lewej wybierz „API i usługi” → „Biblioteka”.
   - Wyszukaj „Search Console API” i kliknij „Włącz”.
4. **Utwórz konto serwisowe:**
   - W menu po lewej wybierz „IAM i administracja” → „Konta serwisowe”.
   - Kliknij „Utwórz konto serwisowe”.
   - Nazwij konto, kliknij „Utwórz i kontynuuj”.
   - Uprawnienia możesz pominąć, kliknij „Gotowe”.
5. **Wygeneruj klucz JSON:**
   - Kliknij na utworzone konto serwisowe na liście.
   - Przejdź do zakładki „Klucze”.
   - Kliknij „Dodaj klucz” → „Utwórz nowy klucz” → wybierz „JSON” → „Utwórz”.
   - Plik JSON zostanie pobrany na Twój komputer – zmień jego nazwę na `indexing-api.json` i umieść w katalogu skryptu.
6. **Dodaj konto serwisowe do Search Console:**
   - Skopiuj adres e-mail konta serwisowego z pliku JSON (pole `client_email`).
   - Wejdź na https://search.google.com/search-console/users i dodaj to konto jako użytkownika (najlepiej z uprawnieniami „Pełny” lub „Właściciel”) do wybranej domeny.

**Bez tych kroków skrypt nie będzie miał dostępu do danych GSC!**

## Użycie
1. Edytuj w skrypcie parametr `siteUrl`, aby ustawić domenę (np. `https://TwojaDomena.pl`).
2. Uruchom skrypt:
   ```bash
   python keywords-gsc.py
   ```
3. Wynik zostanie zapisany w pliku o nazwie `frazy_gsc_<data_start>_<data_koniec>.csv` (np. `frazy_gsc_2024-01-01_2025-05-01.csv`).

## Automatyzacja zakresu dat i paginacja
- Skrypt automatycznie ustala zakres dat od dziś do 16 miesięcy wstecz (maksymalny zakres wspierany przez GSC API).
- Pobieranie odbywa się partiami po 25 000 fraz (paginacja przez `startRow`).
- Wyniki są łączone i eksportowane do jednego pliku CSV.

## Przykład działania
1. Skrypt automatycznie ustala zakres dat.
2. Pobiera wszystkie dostępne frazy w partiach po 25 000, aż do wyczerpania danych.
3. Eksportuje całość do pliku CSV.

## Notatki
- Jeśli nie ma danych w podanym zakresie, skrypt wyświetli odpowiedni komunikat.
- Możesz zmienić domenę edytując parametr `siteUrl` w kodzie.
- Konto serwisowe z pliku `indexing-api.json` musi mieć pełny dostęp do domeny w Search Console.
- Jeśli chcesz pobrać dane dla innej domeny, zmień wartość `siteUrl` i upewnij się, że konto serwisowe ma odpowiednie uprawnienia.

## Rozwiązywanie problemów
- Jeśli pojawia się błąd 403: upewnij się, że konto serwisowe ma pełny dostęp do domeny w Search Console.
- Jeśli pojawia się błąd o nieaktywnej usłudze API: aktywuj Search Console API w Google Cloud Console dla projektu powiązanego z kontem serwisowym.
- Jeśli brakuje pakietów, zainstaluj je poleceniem z sekcji "Przygotowanie środowiska".

---

License: :D

---
Dokumentacja zaktualizowana: 2025-05-01.


