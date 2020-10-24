def faixa_notas(notas):
    resposta=[]
    nota_b = []
    nota_m = []
    nota_a = []
    for i in notas:
        if i < 5:
            nota_a +=1
        elif i > 5 and i <= 7:
            nota_b +=1     
        elif i > 7:
            nota_a +=1
    nota_a.extend(nota_b)
    nota_b.extend(nota_a)
       
notas=[1, 2, 4.2, 5.5, 8, 9]