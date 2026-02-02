import os # moduł dający programowi dostęp do środowiska systemu operacyjnego, w którym program działa
import sys # moduł udostępniający programowi informacje o konkretnym uruchomieniu programu, tj, w jaki sposób i na jakiej platformie systemu operacyjnego program został uruchomiony
import tkinter # biblioteka `tkinter`
from tkinter import ttk # podmoduł `ttk` z biblioteki `tkinter` zawierający nowocześniejsze widżety (komponenty) UI (przyciski, listy rozwijalne itd.), które zapewniają spójny i natywny wygląd aplikacji na różnych systemach operacyjnych
from tkinter import messagebox # okno dialogowe
import requests # moduł potrzebny do wysyłania zapytań HTTP do zewnętrznych API
# Zdefiniuj okno UI aplikacji
class CurrencyConverterApp(tkinter.Tk):
    def __init__(self):
        super().__init__() # Zainicjuj główne okno Tkinter (okno UI aplikacji)
        self._configure_styles() # Wywołaj metodę wewnętrzną klasy służącą do konfiguracji globalnych styli aplikacji
        self._configure_window() # Wywołaj metodę wewnętrzną klasy służącą do konfiguracji parametrów okna UI
        self._create_widgets() # Wywołaj metodę wewnętrzną klasy definiującą widżety (komponenty) UI
        self._layout_widgets() # Wywołaj metodę wewnętrzną klasy służącą do zdefiniowania layoutu aplikacji, czyli do rozmieszczenia w oknie komponentów UI
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
        self.geometry("800x700+300+150") # Ustal wymiary okna UI aplikacji oraz jego położenie na ekranie
        self.title("Konwerter walut") # Nadaj oknu aplikacji tytuł
        self.resizable(False, False) # Zablokuj możliwość zmiany wymiarów okna aplikacji
    # Metoda do definiowania widżetów okna aplikacji
    def _create_widgets(self):
        self.main_heading = ttk.Label(self, text="Konwerter walut", font=("TkDefaultFont", 20, "bold")) # Nagłówek aplikacji wraz z ustawieniami czcionki zdefiniowanymi tylko dla niego
        self.entry_amount_label = ttk.Label(self, text="Podaj kwotę:", style="FieldLabel.TLabel") # Etykieta dla pola do wprowadzenia kwoty
        self.entry_amount = ttk.Entry(self) # Pole do wprowadzenia kwoty
        self.entry_amount.focus_set() # Ustaw kursor bezpośrednio na tym polu, aby poprawić UX (User Experience)
        # Waluty – dane (na start "na sztywno", potem podmienisz na API/JSON)
        self.currencies = ["PLN", "EUR", "USD", "GBP", "CHF"]
        # Waluta "Z"
        self.currency_from_label = ttk.Label(self, text="Waluta \"Z\":", style="FieldLabel.TLabel")
        # Komponent `Combobox` służący do wyboru źródłowej waluty
        self.currency_from_combobox = ttk.Combobox(
            self,
            values=self.currencies,
            state="readonly"
        )
        # Waluta "Do"
        self.currency_to_label = ttk.Label(self, text="Waluta \"Do\":", style="FieldLabel.TLabel")
        # Komponent `Combobox` służący do wyboru docelowej waluty
        self.currency_to_combobox = ttk.Combobox(
            self,
            values = self.currencies,
            state="readonly"
        )
        # Ustaw domyślne wartości dla list rozwijalnych (komponentów `Combobox` umożliwiających wybór waluty)
        self.currency_from_combobox.set("PLN")
        self.currency_to_combobox.set("EUR")
        # Przycisk odpowiadający za przeliczenie kwoty z jednej waluty na drugą. Po jego kliknięciu dokona się również walidacja danych wprowadzonych do pola z kwotą oraz pól `Combobox`
        self.convert_button = ttk.Button(self, text="Konwertuj", width=20)

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

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop() # Uruchom aplikację

print(sys.version) # Wypisz, z poziomu kodu, dokładną wersję interpretera Pythona wraz z datą kompilacji oraz nazwą kompilatora
