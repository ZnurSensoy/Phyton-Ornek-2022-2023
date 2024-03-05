sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
# for i in sayilar:
#     print(i)
# i=0
# while(i<len(sayilar)):
#     print(sayilar[i])
#     i+=1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
# baslangic=int(input('Başlangıç Sayısı:'))
# bitis=int(input('Bitiş Sayısı:'))

# i=baslangic
# while i<bitis:
#     i+=1
#     if(i%2==1):
#         print(i)

# 3: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
# sayilar=[]
# i=0
# while i<5:
#     sayi=int(input('Bir sayı giriniz..:'))
#     sayilar.append(sayi)
#     i+=1
# sayilar.sort()
# print(sayilar)

# 4: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (ad, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda for ile listeleyin.

urunler=[]
adet=int(input('Kaç ürün eklemek istiyorsunuz..:'))
i=0
while(i<adet):
    adi=input('ürün ismi:')
    fiyati=input('ürün fiyatı:')
    urunler.append({
        'adi':adi,
        'fiyati':fiyati
    })
    i+=1
for urun in urunler:
    print(f'ürün adı: {urun["adi"]} ürün fiyatı: {urun["fiyati"]}')
