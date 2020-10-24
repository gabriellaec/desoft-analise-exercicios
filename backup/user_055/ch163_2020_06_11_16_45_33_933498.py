def calcula_media(lista_dict):
    lista_notas = []
    qtd = 0
    for d in lista_dict:
        for notas in d.values():
            lista_notas.append(notas)
            qtd += 1
    return (sum(notas)/qtd)
    
            
            