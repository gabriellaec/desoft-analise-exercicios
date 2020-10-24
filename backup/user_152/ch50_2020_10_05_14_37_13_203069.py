def junta_nome_sobrenome(nome, sobre):
    size1 = len(nome)
    size2 = len(sobre)
    space = " "
    juntos = []
    i = 0
    if size1 == size2:
        while i<size1:
            juntos.append(nome[i]+space+sobre[i])
            i +=1
    return juntos