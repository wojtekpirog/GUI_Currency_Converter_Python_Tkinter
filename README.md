# Kalkulator walut z interfejsem graficznym (GUI)
## Imię i nazwisko autora: Wojciech Piróg
## Numer indeksu autora: 62222
## Wersja interpretera Python: 3.10.12

## Opis działania aplikacji:
Aplikacja dokonuje konwersji kwoty pieniężnej w walucie wybranej przez użytkownika z listy do odpowiadającej jej kwoty w innej walucie.
Konwersja odbywa się przy użyciu aktualnych kursów wymiany.
Do pobierania aktualnych informacji o kursach walut aplikacja korzysta z API Narodowego Banku Polskiego (NBP Web API).
Nie jest możliwe wybranie tej samej waluty jako waluty źródłowej i docelowej.
W pole do wprowadzenia kwoty pieniężnej możliwe jest wprowadzenie jedynie wartości liczbowych typu ```float``` lub ```int```. Aplikacja nie przyjmuje jako dane wejściowe liter ani znaków specjalnych.