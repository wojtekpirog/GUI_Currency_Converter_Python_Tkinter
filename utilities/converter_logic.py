# Zaimportuj moduł `Decimal`, który zamienia liczby na typ `Decimal` celem zwiększenia ich precyzji
from decimal import Decimal, ROUND_HALF_UP

def calculate_exchange(amount: Decimal, rate_from: Decimal, rate_to: Decimal) -> Decimal:
    """
    Metoda pomocnicza obsługująca matematyczną logikę konwersji.
    Przyjmuje ona liczby jako obiekty klasy Decimal i zwraca zaokrąglony wynik również jako obiekt klasy Decimal
    """
    if rate_to == 0:
        return Decimal("0.00")
    # Oblicz wynik konwersji
    calculation_result = (amount * rate_from) / rate_to
    """
    Zwróć wynik konwersji jako liczbę zaokrągloną do dwóch miejsc po przecinku.
    Niech trzecia liczba po przecinku zaokrągli wartość drugiej liczby w górę
    """
    calculation_result = calculation_result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return calculation_result