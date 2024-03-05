# Dictionary ler, veri değerlerini 'key':'value' çiftlerinde depolamak için kullanılır.
# key - value
# 42 => konya  34 => istanbul
# sehirler=['konya', 'istanbul']
# plakalar=[42,34]
# print(plakalar[sehirler.index('istanbul')])
# print(plakalar['konya'])
# print(plakalar['istanbul'])

# plakalar={'konya':42, 'istanbul':34}
# print(plakalar['konya'])
# print(plakalar['istanbul'])
# plakalar['ankara']=6
# print(plakalar)
# plakalar['konya']=24
# print(plakalar)

kullanicilar={
    'alican':{
        'yas':36,
        'roller':['kullanici','yonetici'],
        'eposta':'alican@gmail.com',
        'adres':'konya',
        'tel':'123456789'
    },
    'velican':{
        'yas':15,
        'roller':['kullanici'],
        'eposta':'velican@gmail.com',
        'adres':'konya',
        'tel':'123456789'
    }
}
print(kullanicilar['velican'])
print(kullanicilar['velican']['yas'])
print(kullanicilar['velican']['eposta'])
print(kullanicilar['velican']['adres'])
print(kullanicilar['alican']['roller'][0])