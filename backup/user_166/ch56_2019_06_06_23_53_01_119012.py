def calcula_total_da_nota(preço, quantidade):
    contador = 0 
    nota = 0
    while contador < len (preço):
        nota += preço[contador] * quantidade[contador]
        contador +=1
    return nota

        
    