import os # moduł dający programowi dostęp do środowiska systemu operacyjnego, w którym program działa
import sys # moduł udostępniający programowi informacje o konkretnym uruchomieniu programu, tj, w jaki sposób i na jakiej platformie systemu operacyjnego program został uruchomiony
import tkinter # biblioteka `tkinter`
from tkinter import ttk # podmoduł `ttk` z biblioteki `tkinter` zawierający nowocześniejsze widżety (komponenty) UI (przyciski, listy rozwijalne itd.), które zapewniają spójny i natywny wygląd aplikacji na różnych systemach operacyjnych
from tkinter import messagebox # okno dialogowe
import requests # moduł potrzebny do wysyłania zapytań HTTP do zewnętrznych API
# Zdefiniuj okno UI aplikacji
class CurrencyConverterApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self._configure_window()
    # Metoda do konfiguracji okna aplikacji
    def _configure_window(self):
        self.geometry("800x700+300+150") # Ustal wymiary okna UI aplikacji oraz jego położenie na ekranie
        self.title("Konwerter walut") # Nadaj oknu aplikacji tytuł
        self.resizable(False, False) # Zablokuj możliwość zmiany wymiarów okna aplikacji

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
