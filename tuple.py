list=[1,2,3]
tuple=(1,'iki',3.0)
print(type(list))
print(type(tuple))
print(list[2])
print(tuple[2])
print(len(list))
print(len(tuple))
list=['ali', 'veli']
tuple=('damla', 'ayşe', 'ayşe')
list[0]='ahmet'
print(list)
# tuple[0]='deniz'
print(tuple)
print(tuple.count('ayşe'))
print(tuple.index('damla'))
isimler=('demet','emel','ayşe')+tuple
print(isimler)