# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a=int(input('A sayısını gir :'))
# b=int(input('B sayısını gir :'))

# result = (a > b)
# print(f'a:{a} b:{b} den büyüktür : {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# vize1 = float(input('1. Vize: '))
# vize2 = float(input('2. Vize: '))
# final = float(input('Final: '))
# ortalama = ((((vize1+vize2)*0.60)/2) + (final * 0.40))
# print(ortalama)


# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1 = float(input('1. Vize: '))
# vize2 = float(input('2. Vize: '))
# final = float(input('Final: '))
# ortalama = ((((vize1+vize2)*0.60)/2) + (final * 0.40))
# print(f'Ortalamanız {ortalama} dersten geçtiniz: {ortalama >=50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sayi = float(input('Bir sayı giriniz :'))

# tekcift = (sayi % 2 ==0) 

# print(f'girilen sayı cift: {tekcift}')


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# sayi = float(input('Bir sayı giriniz :'))

# ppzitifmi = (sayi > 0) 

# print(f'girilen pozitif: {ppzitifmi}')

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#(email: email@sadikturan.com parola:abc123|)

email= 'email@sadikturan.com'
parola='abc123|'

girilenemail = input('email: ')
girilenpassword = input('Şifre :')

isEmail = (email == girilenemail)
isPasward = (parola == girilenpassword)

print(f'email bilgisi doğru: {isEmail} girilen şifre doğrumu: {isPasward}')


