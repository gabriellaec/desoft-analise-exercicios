li = [3, 4, 5, 6, 7, 9]
a = []

def faixa_notas(li):
    i = 0
    while i < len(li):
        if li[i] < 5:
            a.append (li[i])
    i += 1
    
    return a