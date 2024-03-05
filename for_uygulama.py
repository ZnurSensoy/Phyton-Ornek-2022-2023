sayilar = [1,3,5,7,9,12,16,24]

# 1- Sayilar listesindeki hangi sayılar 3'e ve 4'e tam bölünür?
for sayi in sayilar:
    if (sayi%3==0 and sayi%4==0):
        print(sayi)

# 2- Sayilar listesindeki sayıların toplamı kaçtır ?
toplam=0
for sayi in sayilar:
    toplam=toplam+sayi # toplam+=sayi
    print ('Sayiların Tolamı..:',toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)

telefonlar = [
    {'ad':'samsung S6', 'fiyat': '3000' },
    {'ad':'samsung S7', 'fiyat': '4000' },
    {'ad':'samsung S8', 'fiyat': '5000' },
    {'ad':'samsung S9', 'fiyat': '6000' },
    {'ad':'samsung S10', 'fiyat': '7000' }
]

# 4- Ürünlerin fiyatları toplamı nedir ?
toplam=0
for t in telefonlar:
    fiyat=int(t['fiyat'])
    toplam+=fiyat
print('Toplam ürün fiyatı..:',toplam)

# 5- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for t in telefonlar:
    if(int(t['fiyat'])<=5000):
        print(t['ad'])