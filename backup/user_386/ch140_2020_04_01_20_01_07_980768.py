notas=[1, 2, 4.2, 5.5, 8, 9]
def faixa_notas(notas):
    nota_b = []
    nota_m = []
    nota_a = []
    for i in notas:
        if i < 5:
            nota_b +=1
        elif i > 5 and i <= 7:
            nota_m +=1     
        else:
            nota_a +=1
    nota_b.extend(nota_m)
    nota_m.extend(nota_a)
    
    return nota_b
       