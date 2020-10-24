def lista_primos(n):
    lista = []
    a = 0
    while a <= len(lista):
        if (n == 0) or (n == 1):
            print('não primo')
        elif n == 2:
            a += 1
            if len(lista) <= n:
                lista.append(n)
        else:
            i = n-2
            if n % 2 == 0:
                print('não primo')
            while i>1:
                if n % i == 0:
                    print('não primo')
                i -= 2
                if i == 0:
                    a += 1
                    if len(lista) <= n:
                        lista.append(n)
                        
            return lista
    
    