# # 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=['Bmw','Mercedes','Opel','Mazda']
# print(arabalar)
# # 2-  Liste Kaç elemanlıdır ?
# sonuc=len(arabalar)
# print(sonuc)
# # 3-  Listenin ilk ve son elemanı nedir ?
# sonuc=arabalar[-1]
# print(sonuc)
# # 4-  Mazda değerini Toyota ile değiştirin.
# arabalar[-1]='Toyota'
# print(arabalar)
# # 5-  Mercedes listenin bir elemanı mıdır ?
# sonuc='Mercedes' in arabalar
# print(sonuc)
# # 6-  Listenin -2 indeksindeki değer nedir ?
# sonuc=arabalar[-2]
# print(sonuc)
# 7-  Listenin ilk 3 elemanını alın.
sonuc=arabalar[0:3]
sonuc=arabalar[:3]
sonuc=arabalar[-2:]
print(sonuc)
# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2:]=['Toyota','Renault']
# print(arabalar)
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
sonuc=arabalar+['Audi','Nissan']
# print(sonuc)
# 10- Listenin son elemanını silin.
del arabalar[-1]
sonuc=arabalar
print(arabalar)
# 11- Liste elemanlarını tersten yazdırınız.
sonuc=arabalar[::-1]
print(sonuc)
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 
      # ogrenciA: Ali Can 2010, (70,60,70)
      # ogrenciB: Alper Toy  1999, (80,80,70)
      # ogrenciC: Ahmet Turan 1998, (80,70,90) 
ogrenciA=['Ali','Can',2005,[70,60,70]]
ogrenciB=['Alper','Toy',1999,[80,80,70]]
ogrenciC=['Ahmet','Turan',1998,[80,60,90]]
# 13- Liste elemanlarını ekrana yazdırınız.
print(ogrenciA)
print(ogrenciB)
print(ogrenciC)
# 14- Öğrenci A nın yaşını ve not ortalamasını yazdırınız
sonuc=f"{ogrenciA[0]} {ogrenciA[1]} {2023-ogrenciA[2]} yaşında ve not ortalaması {(ogrenciA[3][0]+ogrenciA[3][1]+ogrenciA[3][2])/3}"
print(sonuc)