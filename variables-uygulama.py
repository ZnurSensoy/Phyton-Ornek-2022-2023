"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""
musteriAdi='Ali'
musteriSoyadi='Can'
musteriAdSoyad=musteriAdi+' '+musteriSoyadi
print(musteriAdSoyad)
musteriCinsiyet=True    # Erkek
musteriTcKimlik='12554644848'
musteriDogumYili=1986
musteriAdresi='Konya Meram'
musteriYasi=2023-musteriDogumYili
print(musteriYasi)


"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""
siparis1=110
siparis2=1100.5
siparis3=356.95

toplam=siparis1+siparis2+siparis3
print('Siparişlerin Toplamı..:',toplam)
