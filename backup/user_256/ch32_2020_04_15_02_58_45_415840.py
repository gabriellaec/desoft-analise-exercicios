def  lista_primos(n):
    if n==1:
        return "2"
    else:
        i = 0
        primo = 3
        listadeprimos =[]
        while i<=n:
            listadeprimos.append(primo)
            primo+=2
            i+=1
    return listadeprimos
        
        