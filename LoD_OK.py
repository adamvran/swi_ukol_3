class BatteryStatus:
    def __init__(self):
        # Inicializujeme hloubku vybití na 0%. Na začátku je baterie plně nabita.
        self.depth_of_discharge = 0

    def is_low(self):
        # Tato metoda zjistí, jestli je baterie vybitá.
        # Definujeme, že baterie je vybitá, pokud je hloubka vybití větší než 80%.
        # Tímto způsobem skrýváme interní detaily o tom, co to znamená být vybitá.
        return self.depth_of_discharge > 80


class Battery:
    def __init__(self):
        # Každá baterie má svůj vlastní stav, který je reprezentován instancí třídy BatteryStatus.
        self.status = BatteryStatus()

    def is_battery_low(self):
        # Tato metoda zjistí, jestli je baterie vybitá.
        # Neptáme se přímo na hloubku vybití, ale ptáme se na vyšší úrovni abstrakce,
        # jestli je baterie nízko vybitá. To je v souladu se Zákonem Demeter,
        # protože nevíme, jak je "vybitá" definováno v třídě BatteryStatus.
        return self.status.is_low()


battery = Battery()
# Zjistíme, jestli je baterie vybitá. Očekáváme False, protože baterie byla právě inicializována
# a její hloubka vybití je na 0%.
print(battery.is_battery_low())
