t = 1
maior = 0
t_maior = 0 
while t < 1001:
    colatz_t = [t]
    num = t
    while num != 1:
        if num == 2:
            num = num/2
            colatz_t.append(num)   
        elif num % 2 == 0:
            num = num/2
            colatz_t.append(num)
        elif num % 2 != 0:
            num = 3*num + 1
            colatz_t.append(num)
    if len(colatz_t) > maior:
        maior = len(colatz_t)
        t_maior = t 
    
    t += 1
print(t_maior)