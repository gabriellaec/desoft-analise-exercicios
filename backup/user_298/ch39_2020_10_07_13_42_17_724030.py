t = 1
maior = 0
t_maior = 0 
while t < 1001:
    colatz_t = t
    num = t
    w = 0
    while num != 1:
        if num == 2:
            num = num/2
            w += 1  
        elif num % 2 == 0:
            num = num/2
            w += 1
        elif num % 2 != 0:
            num = 3*num + 1
            w += 1
    if w > maior:
        maior = w
        t_maior = t 
    
    t += 1
print(t_maior)