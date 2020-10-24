def junta_nome_sobrenome(nome, sobrenome):
    lista = list()
    for i in range(len(nome)):
        nome_sobr = [nome[i], sobrenome[i]]
        lista.append(nome_sobr) 
    for i in range(len(lista)):      
        return('{0} {1}'.format(lista[i][0], lista[i][1]))