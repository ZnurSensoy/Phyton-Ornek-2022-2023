# x=10
# sonuc = 5 < x < 10
# sonuc = (x>5) and (x<10)
# and
# True and True => True
# True and False => False
# False and True => False
# False and False => False

# hak=0
# devam='e'
# sonuc= (hak>0) and (devam=='e')

# or
# x=-5
# sonuc = (x>0) or (x%2==0)
# True or False => True
# True or True => True
# False or True => True
# False or False => False
# print(sonuc)

# not => değil
# x=5
# sonuc=not(x>0)
# print(sonuc)

# 1- x değişkenine atanan değer 5 ile 10 arasında olan bir çift sayı mıdır?
# x=7
# sonuc=((x>5) and (x<10)) and (x%2==0)
# print(sonuc)
# 2- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi=float(input('Sayı giriniz..:'))
# sonuc=(sayi>0) and (sayi<=100)
# print(f'sayı 0-100 arasında mı?: {sonuc}')
# 3- Girilen üç sayıyı büyüklük olarak karşılaştırınız.
a=int(input('A syısını giriniz..:'))
b=int(input('B syısını giriniz..:'))
c=int(input('C syısını giriniz..:'))
sonuc=(a>b) and (a>c)
print(f'A sayısı en büyük sayıdır: {sonuc}')
sonuc=(b>a) and (b>c)
print(f'B sayısı en büyük sayıdır: {sonuc}')
sonuc=(c>a) and (c>b)
print(f'C sayısı en büyük sayıdır: {sonuc}')