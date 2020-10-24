def faixa_notas(lista):
    abaixo=0
    media=0
    acima=0
    for a in lista:
        if a<5:
            abaixo+=1
        elif a<=7:
            media+=1
        else:
            acima+=1
            
lista_de_alunos=[abaixo,média,acima]
return lista_de_alunos