maior = []
rascunho = []
cont = 1000

while cont > 0:
    
    num = cont
    while num != 1:
        rascunho.append(num)
        if num % 2 == 0:
            num = num / 2
            rascunho.append(num)
        else:
            num = (3 * num) + 1
            rascunho.append(num)
    
    if len(rascunho) > len(maior):
        maior = rascunho.copy()
    rascunho.clear()
    cont -= 1