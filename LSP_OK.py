class Battery:
    def get_status(self):
        return "Battery status: OK"


class RechargeableBattery(Battery):
    def charge(self):
        return "Rechargeable battery charging..."


class NonRechargeableBattery(Battery):
    # Tato třída není vybavena metodou charge, což odpovídá realitě
    pass


# Demonstrace použití
battery = RechargeableBattery()
print(battery.charge())  # V pořádku, baterie je nabíjecí

non_rechargeable = NonRechargeableBattery()
# Následující řádek nevyvolá metodu charge, protože non_rechargeable nemá takovou metodu
print(non_rechargeable.get_status())
