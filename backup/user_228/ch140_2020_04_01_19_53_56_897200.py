def faixa_notas(lista):
    abaixo=0
    média=0
    acima=0
    for a in lista:
        if a<5:
            abaixo=abaixo+1
        elif a<=7:
            média=média+1
        else:
            acima=acima+1
            
lista_de_alunos=[abaixo,média,acima]
return lista_de_alunos