def fatorial(x):
    result=1
    for i in range(x):
        result=result*(x-i)
    return result

def calcula_euler(x,n):
    i = 0
    soma = 1
    while i < n:
        soma += (x ** (i)) / fatorial(i)
        i += 1        
    return soma

# mesma funcao usando FOR

#def calcula_euler(x,n):
#    soma = 0
 #   for i in range(n):
  #      soma += (x ** (i)) / fatorial(i)       
        
   # return soma