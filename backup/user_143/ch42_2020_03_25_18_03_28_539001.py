palavra1 = str(input('palavra:'))
palavra2 = str(input('palavra:'))
palavra3 = str(input('palavra:'))
palavra4 = str(input('palavra:'))
lista=[]
invalid True
while invalid:
    prim_letra=palavra1[0]
    prime_letra=palavra2[0]
    primei_letra=palavra3[0]
    primeir_letra=palavra4[0]
    if prim_letra == 'a':
        lista.append(palavra1)
        print(palavra1)
    elif prime_letra == 'a':
        lista.append(palavra2)
        print(palavra2)
    elif primei_letra == 'a':
        lista.append('palavra3')
        print(palavra1)
    elif primeir_letra == 'a':
        lista.append('palavra4')        
        print(palavra1)
    else:
        print('fim')
        print(lista)
        invalid False
    
        