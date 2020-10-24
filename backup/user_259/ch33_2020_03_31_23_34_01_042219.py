def primos_entre(a,b):
    primos = []
    nao_primos = []
    for num in range(a, b+1):
        if num>1:
            for i in range (2, num+1):
                if (num%i) == 0:
                    if num==2:
                        primos.append(num)
                    else:
                        break
                else:
                    primos.append(num)
    return (len(primos))
           
     
                
