import random
din = 100


while din <0:
    tipo = input('digite o tipo da aposta [n ou p]')
    val = int(input('quanto quer apostar?))
    num = random.randint(36)
    
    
    if tipo == 'n':
        chute = int(input('digite um n de 1 a 36'))
        if chute ==num:
            din += 36*val
        else:
            din -=val
    elif tipo =='p':
        par_i = input('p ou i')
        
        if num % 2 == 0:
            certo = 'p'
        else:
            certo = 'i'
        
        if par_i == certo:
            din += val
        else:
            din -= val
        
    