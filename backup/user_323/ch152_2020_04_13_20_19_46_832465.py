def verifica_preco(Nome, Livro, Cor):
    if Nome in Livro:
        cor=Livro[Nome]
        if cor in Cor:
            Preço= Cor[cor]
            return Preço
       
