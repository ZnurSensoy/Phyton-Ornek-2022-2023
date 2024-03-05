# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz (Ehliyet alma koşulu yaş en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır).
# isim=input('Adınız..:')
# yas=int(input('Yaşınız..:'))
# egitim=input('Eğitim durumu..:')
# if (yas>=18):
#     if (egitim=='lise') or (egitim=='üniversite'):
#         print(f'{isim} ehliyet alabilirsin.')
#     else:
#         print(f'{isim} ehliyet alamazsın, eğitim durumun yetersiz.')
# else:
#     print(f'{isim} ehliyet alamazsın, yaşın tutumuyor')

# 2- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
# import datetime
# tarih=input('Aracın Trafiğe Çıkış Tarihi (2023/4/6):')
# tarih=tarih.split('/')
# trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi=datetime.datetime.now()
# fark=simdi-trafigeCikis
# gun=fark.days
# if gun<=365:
#     print('1. servis aralığı')
# elif gun>365 and gun<=365*2:
#     print('2. servis aralığı')
# elif gun>365*2 and gun<=365*3:
#     print('3. servis aralığı')
# else:
#     print('hatalı süre')


# 3- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a=int(input('A sayısını giriniz..:'))
b=int(input('B sayısını giriniz..:'))
c=int(input('C sayısını giriniz..:'))
if (a>b) and (a>c):
    print(f'A en büyük sayıdır. {a}')
elif (b>a) and (b>c):
    print(f'B en büyük sayıdır. {b}')
elif (c>b) and (c>a):
    print(f'C en büyük sayıdır. {c}')