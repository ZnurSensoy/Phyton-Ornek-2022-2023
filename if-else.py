# if 3>2:
#     print('Hoş geldiniz')

kullanici_adi=input('Kullanici Adı:')
sifre=input('Şifre:')
# if (kullanici_adi=='alican') and (sifre=='1234'):
#     print('Hoş geldiniz')
# else:
#     print('Kullanıcı adı veya şifre yanlış')
if (kullanici_adi=='alican'):
    if (sifre=='1234'):
        print('Hoş geldiniz')
    else:
        print('sifre yanlış')
else:
    print('Kullanıcı adı yanlış')