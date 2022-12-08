print("SELAMAT DATANG DI PROGAM PEMBUAT PIRAMIDA BERULANG")
angka = int(input("Masukan Angka : "))
print(' '*(angka-2),"*")
for z in range ((angka-2),0,-1):
    print(' '*(z-1),"**")
print("**"*angka)