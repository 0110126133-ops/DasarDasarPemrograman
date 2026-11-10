#nomor 1
def celcius_ke_fahrenheit(celcius):
    hasil=(celcius*(9/5))+32
    print(hasil)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

#nomor 2
def is_genap(bilangan):
    print(bilangan % 2 == 0)

is_genap(4)
is_genap(7)

#nomor 3
def nilai(skor):
    if skor >= 80:
       print("lulus")
    elif skor <= 60:
        print("gagal")
    else :
        print("nilai kamu pas pasan")

nilai(88)
nilai(70)
nilai(50)

#nomor 4
def bilangan(angka):
    for i in range(1, angka + 1):
        if i % 2 != 0:
            print(i, end="")
 
bilangan(20)








