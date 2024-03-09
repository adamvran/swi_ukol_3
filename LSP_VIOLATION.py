class Battery:
    def get_status(self):
        return "Battery status: OK"


class RechargeableBattery(Battery):
    def charge(self):
        return "Rechargeable battery charging..."


class NonRechargeableBattery(Battery):
    # Přepisujeme metodu charge, což je nesprávně pro ne-přebíjecí baterie
    def charge(self):
        raise Exception("Non-rechargeable batteries cannot be charged!")


# Demonstrace použití
battery = RechargeableBattery()
print(battery.charge())  # V pořádku, baterie je nabíjecí

non_rechargeable = NonRechargeableBattery()
try:
    print(non_rechargeable.charge())  # Vyvolá výjimku, což je nesprávné chování
except Exception as e:
    print(e)
