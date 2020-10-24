def faixa_notas(notas):
    new_list = []
    s = 0
    for i in range(len(notas)):
        if notas[i] < 5:
            s += 1
            new_list.append(s)
            
        elif notas[i] > 5 and notas[i] < 7:
            s += 1
            new_list.append(s)
            
        elif notas[i] > 7:
            s += 1
            new_list.append(s)