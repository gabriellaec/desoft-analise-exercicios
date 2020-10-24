palavra1 = str(input('palavra:'))
palavra2 = str(input('palavra:'))
palavra3 = str(input('palavra:'))
palavra4 = str(input('palavra:'))
lista=[]
prim_letra=palavra1[0]
prime_letra=palavra2[0]
primei_letra=palavra3[0]
primeir_letra=palavra4[0]
i=0
while(i<1):
    if prim_letra == 'a':
        lista.append(palavra1)
        print(palavra1)
        i+=1
    if prime_letra == 'a':
        lista.append(palavra2)
        print(palavra2)
        i+=1
    if primei_letra == 'a':
        lista.append(palavra3)
        print(palavra3)
        i+=1
    if primeir_letra == 'a':
        lista.append(palavra4)        
        print(palavra4)
        i+=1
    else:
        i+=1
    print(lista)
print('fim')  