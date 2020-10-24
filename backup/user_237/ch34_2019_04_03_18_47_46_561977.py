deposito_inicial = float(input("Qual é o deposito inicial?:"))
juros = float(input("Qual é o juros?:"))
n = 25
total_juros = 0
montante = 0
for e in range(1,n):
    montante = deposito_inicial*(juros+1)**e
    if e == 1:
        total_juros += montante - deposito inicial
    else:
        total_juros += montante - (deposito_inicial*(juros+1)**(e-1))
    print(montante)
    
print(total_juros)
                                   
      
        
    
    
   