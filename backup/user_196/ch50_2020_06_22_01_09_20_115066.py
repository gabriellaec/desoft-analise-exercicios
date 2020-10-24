def junta_nome_sobrenome(listanom,listasob):
    listafinal = []
    for i in range (0, len(listanom)):
        listafinal.append(listanom[i] + (" ") + listasob[i])
    return listafinal
