def celcius_ke_reamur(suhu):
  """Konversi suhu dari Celcius ke Reamur.

  Args:
    suhu: Suhu dalam satuan Celcius.

  Returns:
    Suhu dalam satuan Reamur.
  """

  return suhu * 4 / 5  # Fixed the conversion formula


def celcius_ke_fahrenheit(suhu):
  """Konversi suhu dari Celcius ke Fahrenheit.

  Args:
    suhu: Suhu dalam satuan Celcius.

  Returns:
    Suhu dalam satuan Fahrenheit.
  """

  return (suhu * 9 / 5) + 32


def celcius_ke_kelvin(suhu):
  """Konversi suhu dari Celcius ke Kelvin.

  Args:
    suhu: Suhu dalam satuan Celcius.

  Returns:
    Suhu dalam satuan Kelvin.
  """

  return suhu + 273.15


def main():
  suhu = float(input("Masukkan suhu dalam satuan Celcius: "))

  reamur = celcius_ke_reamur(suhu)
  fahrenheit = celcius_ke_fahrenheit(suhu)
  kelvin = celcius_ke_kelvin(suhu)

  print("Suhu dalam satuan Reamur:", reamur)
  print("Suhu dalam satuan Fahrenheit:", fahrenheit)
  print("Suhu dalam satuan Kelvin:", kelvin)


if __name__ == "__main__":
  main()
