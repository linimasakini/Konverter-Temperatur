#latihan konversi temperatur

#program konversi celcius ke satuan lain
print("PROGRAM KONVERSI TEMPERATUR\n")
print("PROGRAM KONVERSI CELCIUS KE TEMPERATUR LAIN")
celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ", celcius, "derajat celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "derajat reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam reamur adalah ", fahrenheit, "derajat fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam reamur adalah ", kelvin, "derajat kelvin")


print("PROGRAM KONVERSI REAMUR KE TEMPERATUR LAIN")

reamur = float(input("Masukkan suhu dalam reamur : "))
print("Suhu adalah ", reamur, "Derajat reamur")

#celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah", celcius, "derajat celcius")

#fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "derajat fahrenheit")

#kelvin
kelvin = ((5/4) * reamur)+273
print("suhu dalam kelvin adalah", kelvin, "derajat kelvin")

print("PROGRAM KONVERSI FAHRENHEIT KE TEMPERATUR LAIN")

fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("suhu adalah", fahrenheit, "derajat fahrenheit")

#celcius
celcius = (5/9) * (fahrenheit -32)
print("suhu adalah", celcius, "derajat celcius")


#reamur
reamur = (4/9) * (fahrenheit -32)
print("suhu adalah", reamur, "derajat reamur")

#kelvin
kelvin = celcius + 273
print("suhu adalah", kelvin, "derajat kelvin")


print("PROGRAM KONVERSI KELVIN KE TEMPERATUR LAIN")

kelvin = float(input("Masukkan suhu dalam kelvin : "))
print("suhu adalah", kelvin, "derajat kelvin")

#celcius
celcius = kelvin - 273
print("suhu adalah", celcius, "derajat celcius")

#reamur
reamur = (4/5) * (kelvin - 273)
print("suhu adalah", reamur, "derajat reamur")

#fahrenheit
fahrenheit = (4/5) * celcius
print("suhu adalah", fahrenheit, "derajat fahrenheit")
