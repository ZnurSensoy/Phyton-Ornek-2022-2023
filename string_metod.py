mesaj='Merhaba, benim adım Ali Can'
# mesaj=mesaj.upper()
# mesaj=mesaj.lower()
# mesaj=mesaj.title()
# mesaj=mesaj.capitalize()
# mesaj=mesaj.strip()
# mesaj=mesaj.split(',')
# mesaj='-'.join(mesaj)
# aranan=mesaj.find('Ali')
aranan=mesaj.startswith('O')
aranan=mesaj.endswith('k')
# print(aranan)
# mesaj=mesaj.replace('Ali', 'Veli')
# mesaj=mesaj.replace('e', '*')
mesaj=mesaj.center(50,'*')
print(mesaj)