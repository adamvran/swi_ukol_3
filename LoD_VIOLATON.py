class BatteryStatus:
    def __init__(self):
        # Inicializujeme hloubku vybití na 0%. Na začátku je baterie plně nabita.
        self.depth_of_discharge = 0

    def get_depth_of_discharge(self):
        # Tato metoda vrací aktuální hloubku vybití baterie.
        # Hloubka vybití nám říká, kolik energie bylo z baterie již vyčerpáno.
        return self.depth_of_discharge


class Battery:
    def __init__(self):
        # Při vytváření instance Battery vytvoříme také instanci BatteryStatus,
        # která uchovává informace o stavu baterie.
        self.status = BatteryStatus()

    def check_battery_depth(self):
        # Zde přímo přistupujeme k metodě  objektu BatteryStatus,což je porušení Zákona Demeter.
        # Podle tohoto zákona by třída Battery měla komunikovat pouze s objekty, které jsou jejími přímými komponenty
        # a neměla by "řetězit" volání metod (tj. volat metody objektů, které získala
        # z jiných objektů).
        return self.status.get_depth_of_discharge()


battery = Battery()
# Vytiskneme hloubku vybití baterie. Protože jsme baterii právě inicializovali,
# měla by hloubka vybití být 0%.
print(battery.check_battery_depth())  # Toto volání porušuje zákon Demeter
