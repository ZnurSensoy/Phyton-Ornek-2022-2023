
# # 1- Girilen 2 sayıdan hangisi büyüktür ?
# a=int(input('A sayısını giriniz..:'))
# b=int(input('B sayısını giriniz..:'))
# sonuc=(a>b)
# print(f'A: {a} B: {b} den büyüktür: {sonuc}')
# # 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# #    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1=float(input('1. vize..:'))
# vize2=float(input('2. vize..:'))
# final=float(input('Final..:'))
# ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
# print(f'not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sayi=int(input('Bir Sayı Giriniz..:'))
# tekcift=(sayi%2==0)
# print(f'girilen sayının çift olma durumu: {tekcift}')

# 4- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: deneme@demene.com parola:abc123)
email='deneme@deneme.com'
sifre='abc123'

girilenEmail=input('email:')
girilenSifre=input('sifre:')

girilenEmail=(email==girilenEmail.lower().strip())
girilenSifre=(sifre==girilenSifre.lower().strip())

print(f'Email bilgisi doğrumu: {girilenEmail} ve Şifre doğru mu: {girilenSifre}')