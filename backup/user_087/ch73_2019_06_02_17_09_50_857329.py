def remove_vogais(palavra):
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    
    for letra in palavra:
        i = 0
        while i < len(lista_vogais):
            if letra == lista_vogais[i]:
                palavra = palavra.replace(letra, " ")
            i += 1
            nova_palavra = palavra.replace(" ", "")
    return nova_palavra
            
            
            