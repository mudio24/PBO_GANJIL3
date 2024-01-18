class Celcius:

    def __init__(self, suhu):
        self.suhu = suhu

    def get_celcius(self):
        return (self.suhu - 32) * 5 / 9

    def get_fahrenheit(self):
        return self.suhu

    def get_reamur(self):
        return (self.suhu - 32) * 4 / 9

    def get_kelvin(self):
        return (self.suhu - 32) * 5 / 9 + 273


suhu = input("Masukkan suhu dalam fahrenheit:")
C = Celcius(float(suhu))
val = C.get_celcius()
F = C.get_fahrenheit()
R = C.get_reamur()
K = C.get_kelvin()

print(str(val) + " Celcius, sama dengan:")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
