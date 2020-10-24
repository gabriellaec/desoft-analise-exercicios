def quantos_uns (n):
    soma = 0
    i=0
    num = str(n)
    
    while i <= len(num):
        if num[i] == '1':
            soma += 1
            
        i +=1
        
    return soma
                 