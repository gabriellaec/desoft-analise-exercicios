def  lista_primos(n):
    i = 0
    primo = 1
    listadeprimos =[]
    while i<n:
        listadeprimos.append(primo)
        primo+=2
        i+=1
    return listadeprimos
        
        