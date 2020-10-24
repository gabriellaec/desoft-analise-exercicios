def junta_nome_sobrenome(listanom,listasob):
    listafinal = []
    for i in range (0, len(listanom)):
        for b in range (0, len(listasob)):
            listafinal.append(listanom[i] + (" ") + listasob[b])
            return listafinal
