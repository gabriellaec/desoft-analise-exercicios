condicao = True
soma = 0
while condicao :
    
    numero = int(input("Digite um número: "))
    
    
    if numero == 0:
        condicao = False
        print (soma)
        
        
    else:
        soma = soma + numero
        numero = int(input("Digite um número: "))
      
print(soma)