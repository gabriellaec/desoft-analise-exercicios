def verifica_preco(titulo,Dlivros,Dcores):
    if titulo in Dlivros:
        cor= Dlivros[titulo]
        if cor in Dcores:
            preço=Dcores[cor]
            return preço