#DTO (Data Transfer Object) je objekt používaný k přenosu dat mezi různými částmi aplikace.
#Obvykle to jsou jednoduché objekty s několika atributy, které odpovídají datům, která je třeba přenést.

class ZaznamDTO:
    def __init__(self, nazev: str, mnozstvi: str) -> None:
        self.nazev = nazev
        self.mnozstvi = mnozstvi
        return nazev, mnozstvi