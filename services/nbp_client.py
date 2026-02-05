from decimal import Decimal # moduł decimal zapewniający większą precyzję liczb przy kalkulacjach finansowych
import requests # moduł do konstruowania zapytań HTTP i zarządzania danymi pobranymi z API

class RatesClient:
    BASE_URL = "https://api.nbp.pl/api"
    # Metoda klasy służąca do pobierania danych z tabeli A z NBP Web API
    def fetch_table(self):
        # Adres URL, na który zostanie wysłane zapytanie HTTP o najnowszą tabelę A zawierającą informacje o najnowszych kursach średnich walut obcych
        url_address = f"{self.BASE_URL}/exchangerates/tables/A/last/?format=json"
        # Wyślij zapytanie HTTP do serwera
        response = requests.get(url_address, timeout=10)
        response.raise_for_status()
        # Zapisz odpowiedź z serwera jako gotowe dane
        data_ready = response.json()[0]
        # Utwórz słownik zawierający kursy wymiany walut
        rates = {"PLN": Decimal("1.0")}
        for rate in data_ready["rates"]:
            rates[rate["code"]] = Decimal(str(rate["mid"]))
        # Zwróć gotowe dane w postaci słownika zawierającego kursy walut (kody ich nazw oraz średnia cena)
        return rates

# Kod tylko na potrzeby testowania poprawności pobierania danych z NBP Web API
if __name__ == "__main__":
    client = RatesClient()
    rates = client.fetch_table()
    print("Testuję pobieranie danych z tabeli...")
    print("Rates:\n", rates)