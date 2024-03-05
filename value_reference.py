# value tipi => string, number (bellekte verinin kendisi depolanır)
x=5
y=25
x=y
y=10
print(x,y)

# reference veri tipi => list (bellekte verinin adresi depolanır.)

a=['elma','muz']
b=['elma','muz']
a=b
b[0]='üzüm'
print(a,b)
