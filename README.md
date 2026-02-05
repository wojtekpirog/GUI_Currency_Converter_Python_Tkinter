# Kalkulator walut z interfejsem graficznym (GUI)
## Imię i nazwisko autora: Wojciech Piróg
## Numer indeksu autora: 62222
## Wersja interpretera Python: 3.10.12

## Opis działania aplikacji:
Aplikacja desktopowa została napisana w języku Python z wykorzystaniem biblioteki **Tkinter**.
Aplikacja dokonuje konwersji kwoty pieniężnej w walucie wybranej przez użytkownika z listy do odpowiadającej jej kwoty w innej walucie.
Konwersja odbywa się przy użyciu aktualnych kursów wymiany.
Do pobierania aktualnych informacji o kursach walut aplikacja korzysta z API Narodowego Banku Polskiego (**NBP Web API**).

## Funkcje
* Pobieranie najnowszych kursów średnich walut obcych z API,
* Obsługa waluty PLN oraz wielu walut obcych oraz konwersji między nimi,
* Wysoka precyzja obliczeń finansowych dzięki modułowi `decimal`,
* Prosty i intuicyjny interfejs graficzny z walidacją danych wejściowych,
* Oddzielenie warstwy logicznej od warstwy UI interfejsu graficznego.

## Struktura projektu
* `currency_converter.py` – główny plik uruchomieniowy aplikacji,
* `services/nbp_client.py` – klient HTTP do komunikacji z API Narodowego Banku Polskiego,
* `utilities/converter_logic.py` - w tym pliku znajduje się matematyczna logika konwersji,
* `requirements.txt` – plik zawierający wykaz zależności nie będących częścią biblioteki standardowej Pythona

Zgodnie z dobrą praktyką, do folderów `services` oraz `utilities` został dodany pusty plik `__init__.py`, który informuje interpreter języka Python o tym, że te foldery są oficjalnymi pakietami aplikacji.

## Architektura
Projekt został podzielony na moduły `services` oraz `utilities`, dzięki czemu wiadomo, za jaki aspekt aplikacji odpowiada dany plik (fragment kodu źródłowego). Ma to na celu poprawę modularności kodu, a więc także jego utrzymanie.

## Użycie modułu `Decimal`
Po operowania na wartościach liczbowych zdecydowałem się zastosować moduł `decimal` z biblioteki standardowej Pythona. Ma to na celu zwiększenie precyzji zaokrągleń wartości pieniężnych oraz uniknięcie błędów zaokrągleń binarnych, co jest bardzo istotny wpływ na poprawność działania aplikacji finansowych.

## Inne informacje
* Wybranie tej samej waluty jako waluty źródłowej i docelowej skutkuje zwróceniem wyniku o treści na przykład `Wynik: 1 PLN = 1 PLN`,
* Nie jest dozwolone wprowadzenie ciągu znaków zawierającego litery i/lub znaki specjalne,
* Ujemne wartości liczbowe nie są dozwolone

## Sposób instalacji i uruchomienia
Do utworzenia aplikacji użyłem interpretera języka Python w wersji 3.10.12. Upewnij się, że masz go zainstalowego.
Aplikacja wykorzystuje bibliotekę `requests` do wysyłania zapytań HTTP. Zainstaluj ją ją komendą:
```
pip install -r requirements.txt
```
Uruchom program komendą:
```
python currency_converter.py
```
lub:
```
python3 currency_converter.py
```