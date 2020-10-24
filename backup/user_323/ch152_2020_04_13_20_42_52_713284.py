def verifica_preco(Nome, Dicionario, Cor):
    if Nome in Dicionario:
        cor=Dicionario[Nome]
        if cor in Cor:
            Preço= Cor[cor]
            return Preço
       
