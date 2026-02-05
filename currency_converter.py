import os # moduł dający programowi dostęp do środowiska systemu operacyjnego, w którym program działa
import sys # moduł udostępniający programowi informacje o konkretnym uruchomieniu programu, tj, w jaki sposób i na jakiej platformie systemu operacyjnego program został uruchomiony
import tkinter # biblioteka `tkinter`
from tkinter import ttk # podmoduł `ttk` z biblioteki `tkinter` zawierający nowocześniejsze widżety (komponenty) UI (przyciski, listy rozwijalne itd.), które zapewniają spójny i natywny wygląd aplikacji na różnych systemach operacyjnych
from tkinter import messagebox # podmoduł dodający okno dialogowe na potrzeby wyświetlania użytkownikowi komunikatów o błędach
from decimal import Decimal # moduł decimal zapewniający możliwość zamiany ciągów znaków na wartości liczbowe o większej precyzji
from decimal import InvalidOperation # `InvalidOperation` to pakiet modułu `decimal` umożliwiający obsługę wyjątku `InvalidOperation` w bloku `try/except`
# Zaimportuj klasę definiującą zachowanie i działanie klienta HTTP
from services.nbp_client import RatesClient
# Zaimportuj metodę pomocniczą służącą do wykonania matematycznej kalkulacji kwoty
from utilities.converter_logic import calculate_exchange
# Zdefiniuj okno UI aplikacji
class CurrencyConverterApp(tkinter.Tk):
    def __init__(self):
        super().__init__() # Zainicjuj główne okno Tkinter (okno UI aplikacji)
        self.nbp = RatesClient()
        self._configure_styles() # Wywołaj metodę wewnętrzną klasy służącą do konfiguracji globalnych styli aplikacji
        self._configure_window() # Wywołaj metodę wewnętrzną klasy służącą do konfiguracji parametrów okna UI
        self._create_widgets() # Wywołaj metodę wewnętrzną klasy definiującą widżety (komponenty) UI
        self._layout_widgets() # Wywołaj metodę wewnętrzną klasy służącą do zdefiniowania layoutu aplikacji, czyli do rozmieszczenia w oknie komponentów UI
        self._load_rates_from_nbp()
    # Metoda do konfiguracji globalnych styli
    def _configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("default")
        # Nadaj domyślny krój czcionki dla całej aplikacji, korzystając z globalnego selektora "."
        self.style.configure(
            ".",
            font=("TkDefaultFont", 16)
        )
        # Nadaj customową konfigurację kroju czcionki dla etykiet pól
        self.style.configure(
            "FieldLabel.TLabel",
            font=("TkDefaultFont", 12)
        )
    # Metoda do konfiguracji okna aplikacji
    def _configure_window(self):
        self.geometry("1000x800+300+150") # Ustal wymiary okna UI aplikacji oraz jego położenie na ekranie
        self.title("Konwerter walut") # Nadaj oknu aplikacji tytuł
        self.resizable(False, False) # Zablokuj możliwość zmiany wymiarów okna aplikacji
    # Metoda służąca do pobrania kursów walut i ich zdefiniowania w warstwie UI
    def _load_rates_from_nbp(self):
        # Spróbuj pobrać kursy walut. W przypadku wystąpienia błędu wyświetl okno modalne z komunikatem błędu i zakończ działanie metody.
        try:
            exchange_rates = self.nbp.fetch_table()
        except Exception as exception:
            messagebox.showwarning("Błąd", f"Nie udało się pobrać kursów walut z NBP Web API. Informacje o błędzie:\n\n {exception}.")
            return
        # Zapisz wartość (słownik zawierający informacje o kursach walut) zwróconą z funkcji `nbp_client.fetch_table()` w zmiennej
        self.exchange_rates = exchange_rates
        # Zapisz wszystkie klucze ze słownika (kody walut) pod zmienną `rates`, następnie posortuj je i zapisz do zmiennej `currency_codes`
        currency_codes = sorted(exchange_rates.keys())
        # Uzupełnij widżety `Combobox`
        self.currency_from_combobox["values"] = currency_codes
        self.currency_to_combobox["values"] = currency_codes
        # Ustaw domyślne wartości do wyboru w obu widżetach `Combobox`, jeśli to możliwe
        if "PLN" in currency_codes:
            self.currency_from_combobox.set("PLN")
        if "EUR" in currency_codes:
            self.currency_to_combobox.set("EUR")
        
    # Metoda do definiowania widżetów okna aplikacji
    def _create_widgets(self):
        self.main_heading = ttk.Label(self, text="Konwerter walut", font=("TkDefaultFont", 20, "bold")) # Nagłówek aplikacji wraz z ustawieniami czcionki zdefiniowanymi tylko dla niego
        self.entry_amount_label = ttk.Label(self, text="Podaj kwotę:", style="FieldLabel.TLabel") # Etykieta dla pola do wprowadzenia kwoty
        self.entry_amount = ttk.Entry(self) # Pole do wprowadzenia kwoty
        self.entry_amount.focus_set() # Ustaw kursor bezpośrednio na tym polu, aby poprawić UX (User Experience)
        # Waluta "Z"
        self.currency_from_label = ttk.Label(self, text="Waluta \"Z\":", style="FieldLabel.TLabel")
        # Komponent `Combobox` służący do wyboru źródłowej waluty
        self.currency_from_combobox = ttk.Combobox(self, state="readonly")
        # Waluta "Do"
        self.currency_to_label = ttk.Label(self, text="Waluta \"Do\":", style="FieldLabel.TLabel")
        # Komponent `Combobox` służący do wyboru docelowej waluty
        self.currency_to_combobox = ttk.Combobox(self, state = "readonly")
        # Ustaw domyślne wartości dla list rozwijalnych (komponentów `Combobox` umożliwiających wybór waluty)
        self.currency_from_combobox.set("PLN")
        self.currency_to_combobox.set("EUR")
        # Przycisk odpowiadający za przeliczenie kwoty z jednej waluty na drugą. Po jego kliknięciu dokona się również walidacja danych wprowadzonych do pola z kwotą oraz pól `Combobox`
        self.convert_button = ttk.Button(self, text="Konwertuj", width=20, command=self._validate_user_input)
        # Widżet wyświetlający wynik konwersji
        self.result_label = ttk.Label(
            self,
            text = "Wynik: -"
        )
    # Metoda "event handler", która wywoła się w reakcji na naciśnięcie przycisku "Konwertuj"
    def _validate_user_input(self):
        """Metoda wewnętrzna klasy, która przyjmie dane wejściowe od użytkownika: kwotę, walutę \"Z\" i walutę \"Do\".
           Następnie dokona walidacji danych wejściowych i w przypadku pomyślnego przejścia walidacji dokona konwersji wprowadzonej kwoty w walucie \"Z\" do waluty \"Do\"
        """
        amount_str = self.entry_amount.get().replace(",", ".")
        currency_from = self.currency_from_combobox.get()
        currency_to = self.currency_to_combobox.get()
        # Walidacja: Czy użytkownik wprowadził liczbę? Jeśli nie, poproś użytkownika o wprowadzenie liczby dodatniej.
        # Następnie zakończ działanie funkcji
        try:
            amount = Decimal(amount_str)
            # Jeżeli użytkownik wprowadził liczbę ujemną, rzuć wyjątek `ValueError`
            if amount < 0:
                raise ValueError("Kwota nie może być ujemna.")
        except (InvalidOperation, ValueError):
            messagebox.showerror("Niepoprawna wartość", "Wprowadź kwotę jako liczbę dodatnią.")
            return
        # Walidacja: Czy zostały wybrane te same waluty w obu widżetach `Combobox`?
        if currency_from == currency_to:
            messagebox.showinfo("Te same waluty", "Wybrano dwie takie same waluty. Konwersja nie jest konieczna.")
            # Jeżeli użytkownik wybrał dwie te same waluty, wyświetl informację o wyniku konwersji jak na przykład "1 PLN = 1 PLN"
            # Następnie zakończ działanie funkcji
            self.result_label.config(text = f"Wynik: {amount:.2f} {currency_from} = {amount:.2f} {currency_to}")
            return
        # Jeśli walidacja przeszła pomyślnie, przekaż poprawne dane wejściowe do osobnej funkcji, która zajmie się obsługą logiki konwersji
        self._perform_conversion(amount, currency_from, currency_to)

    # Metoda służąca do wywołania logiki konwersji
    def _perform_conversion(self, amount, currency_from, currency_to):
        """
        Metoda wewnętrzna klasy do wykonywania faktycznych obliczeń po walidacji danych wejściowych.
        """
        exchange_rate_from = self.exchange_rates[currency_from]
        exchange_rate_to = self.exchange_rates[currency_to]
        """
        Wywołaj funkcję z pliku `utilities.converter_logic`
        Pobierz wynik kalkulacji zwrócony z funkcji `calculate_exchange`
        """
        calculation_result = calculate_exchange(amount, exchange_rate_from, exchange_rate_to)
        # Wyświetl na ekranie UI wynik kalkulacji
        self.result_label.config(text = f"Wynik: {amount:.2f} {currency_from} = {calculation_result} {currency_to}")


    # Metoda do definiowania layoutu komponentów (widżetów) okna aplikacji
    def _layout_widgets(self):
        self.main_heading.pack(pady=(50, 40))
        self.entry_amount_label.pack(pady=5)
        self.entry_amount.pack(pady=(5, 30))
        self.currency_from_label.pack(pady=5)
        self.currency_from_combobox.pack(pady=(5, 30))
        self.currency_to_label.pack(pady=5)
        self.currency_to_combobox.pack(pady=(5, 40))
        self.convert_button.pack(pady=(5, 30))
        self.result_label.pack(pady=(10, 30))

"""
Spróbuj uruchomić aplikację za pomocą komendy `python currency_converter.py` (lub `python3 currency_converter.py`).
W przypadku wystąpienia błędu podczas startu aplikacji wyświetl w konsoli komunikat z informacjami o błędzie
""" 
if __name__ == "__main__":
    try:
        app = CurrencyConverterApp()
        app.mainloop() # Uruchom aplikację
    except Exception as exception:
        print("Wystąpił błąd podczas startu aplikacji:\n", exception)

print(sys.version) # Wypisz, z poziomu kodu, dokładną wersję interpretera Pythona wraz z datą kompilacji oraz nazwą kompilatora
