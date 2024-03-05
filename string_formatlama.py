ad='Ali'
soyad='Can'
yas=37
print('Benim adım {}'.format(ad))
print('Benim adım {} {}'.format(ad, soyad))
print('Benim adım {0} {1}'.format(ad, soyad))
print('Benim adım {1} {0}'.format(ad, soyad))
print('Benim adım {a} {s}'.format(a=ad, s=soyad))
print('Benim adım {} {} ve ben {} yaşımdayım'.format(ad, soyad,yas))
sonuc=200/700
print('Sonuç..: {}'.format(sonuc))
print('Sonuç..: {s:1.4}'.format(s=sonuc))

print(f'Benim adım {ad} {soyad} ve ben {yas} yaşımdayım')