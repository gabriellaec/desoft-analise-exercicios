numero = int(input("Digite um número: "))

if numero == 0 :
    
    print("A soma desses números é 0")

else:
    
    condicao = True
    soma = 0
    
    while condicao:
        
        numero = int(input("Digite um número: "))
        
        if numero == 0:
            
            condicao = False
            
            print("A soma desses números é {0}".format(soma))
        
        else:
            
            soma += numero