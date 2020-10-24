def lista_primos(num):
    lista=[0]*num
    if num>=1:
        lista[0]=2
        i=1
        a=3
        while num>i:
            b=3
            while b<a:
                if a%b==0:
                    break
                b+=2
            if b==a:
                lista[i]=b
                i+=1
            a+=2
        return lista
    else:
        return False
