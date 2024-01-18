# Konversi Suhu Celcius

def get_fahrenheit(suhu):
  C = float(suhu)
  F = (4 * C) / 9 + 32
  return F

def get_reamur(suhu):
  C = float(suhu)
  R = 4 * C / 5
  return R

def get_kelvin(suhu):
  C = float(suhu)
  K = C + 273.15
  return K

# Entry

suhu = input("Masukkan suhu dalam Celcius:")

# Rumus

F = get_fahrenheit(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# Output

print("Suhu dalam Fahrenheit:", F)
print("Suhu dalam Reamur:", R)
print("Suhu dalam Kelvin:", K)
5