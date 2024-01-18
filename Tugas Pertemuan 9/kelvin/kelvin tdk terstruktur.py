def celcius_ke_reamur(suhu):
  """
  Mengkonversi suhu Celcius ke Reamur.

  Argumen:
    suhu: Suhu dalam satuan Celcius.

  Mengembalikan:
    Suhu dalam satuan Reamur.
  """
  return 4 / 5 * (suhu - 273)

def celcius_ke_fahrenheit(suhu):
  """
  Mengkonversi suhu Celcius ke Fahrenheit.

  Argumen:
    suhu: Suhu dalam satuan Celcius.

  Mengembalikan:
    Suhu dalam satuan Fahrenheit.
  """
  return 9 / 5 * (suhu - 273) + 32

def celcius_ke_kelvin(suhu):
  """
  Mengkonversi suhu Celcius ke Kelvin.

  Argumen:
    suhu: Suhu dalam satuan Celcius.

  Mengembalikan:
    Suhu dalam satuan Kelvin.
  """
  return suhu + 273

def main():
  # Mendapatkan input pengguna
  suhu = float(input("Masukkan suhu dalam satuan Celcius: "))

  # Mengkonversi dan mencetak suhu
  reamur = celcius_ke_reamur(suhu)
  fahrenheit = celcius_ke_fahrenheit(suhu)
  kelvin = celcius_ke_kelvin(suhu)

  print(f"Suhu dalam Reamur: {reamur:.2f}")
  print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f}")
  print(f"Suhu dalam Kelvin: {kelvin:.2f}")

if __name__ == "__main__":
  main()
