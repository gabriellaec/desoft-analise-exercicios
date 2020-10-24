def junta_nome_sobrenome(nome,sobrenome):
    espaco = ' '
    nome_completo =[]
    i=0
    while i < len(nome) and i < len(sobrenome):
        nc = nome+espaco+sobrenome
        nome_completo.append(nc)
        i+=1
