def lista_primos(num):
    lista=[0]*num
    if num < 0:
        print('Negativo')
    else:
        if (num >= 1):
            lista[0]=2
            a = 1
            b = 3
            while a<num:
                c =3
                while c<b:
                    if b%c == 0:
                        break
                    c=c+2
                if c ==b:
                    lista[a]=c
                    a=a+1
                b=b+2
            return lista

z=lista_primos(10)
print(z)
