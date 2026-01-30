import os # moduł dający programowi dostęp do środowiska systemu operacyjnego
import sys # moduł udostępniający systemowi operacyjnemu informacje o uruchomionym programie
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox # okna dialogowe
import requests # moduł potrzebny do wysyłania zapytań HTTP do zewnętrznych API
# Utwórz okno UI aplikacji
class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x450+300+150") # Ustal wymiary okna UI aplikacji oraz jego położenie na ekranie
        self.title("Konwerter walut") # Nadaj tytuł okna aplikacji
        self.resizable(width=0, height=0) # Zablokuj możliwość zmiany wymiarów okna aplikacji

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
