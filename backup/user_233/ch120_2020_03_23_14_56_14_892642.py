from random import randint

dinheiros = 100

while dinheiros > 0:
    
    print(dinheiros)
    
    aposta = float(input('Aposta: '))
    if aposta == 0: break
        
    n_ou_p = input('Número ou paridade? (n/p) ')
    if n_ou_p == 'n': apostado = int(input('Número: '))
    elif n_ou_p == 'p': apostado = input('Par ou ímpar? (p/i) ')
        
   	resultado = randint(0, 36)
    
    if n_ou_p == 'n':
        if apostado == resultado: dinheiros += aposta * 35
        else: dinheiros -= aposta
            
    elif n_ou_p == 'p':
        
        if resultado == 0: dinheiros -= aposta
        elif resultado % 2 == 0: resultado = 'p'
        else: resultado = 'i'
        
        if resultado == apostado: dinheiros += aposta
        if resultado != apostado: dinheiros -= aposta
    
    
    
    