x,y,z = 2,5,10

numbers = 1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# 2- y' nin x' e kalansız bölümünü hesaplayınız.
# 3- (x,y,z) toplamının mod 3' ü nedir ?
# 4- y' nin x. kuvvetini hesaplayınız.
# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?


# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# sayi1=float(input("Bir sayı girin:"))
# sayi2=float(input("Bir sayı girin:"))
# fark = (sayi1*sayi2)-(x+y+z)
# print("Fark :",fark)

# 2- y' nin x' e kalansız bölümünü hesaplayınız.

# bolme = y // x
# print(bolme)

# 3- (x,y,z) toplamının mod 3' ü nedir ?

# deger = (x+y+z) %3
# print(deger)


# 4- y' nin x. kuvvetini hesaplayınız.
# deger = y ** x

# print(deger)

# x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?

# x, *y,z = numbers

# print(x,y,z)
# print(z**3)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
x, *y,z = numbers
deger = y[0]+y[1]+y[2]
print(deger)
