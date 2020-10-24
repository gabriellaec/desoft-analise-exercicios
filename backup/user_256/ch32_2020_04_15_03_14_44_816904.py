def  lista_primos(n):
    if n==1:
        return [2]
    else:
        i = 1
        impares = 1
        primo = 3
        listadeprimos =[2]
        while i<=n:
            listadeprimos.append(primo)
            while primo%2==0 or primo%impares==0:
                primo+=2  
                impares+=2
            i+=1
    return listadeprimos
       
        
        