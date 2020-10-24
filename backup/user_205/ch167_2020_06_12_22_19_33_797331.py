def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for keys,lista in dicionario.items():
        for numeros in lista[6:]:
                if keys in dic:
                    dic[keys] += numeros
                else: 
                    dic[keys] = numeros
    return dic

def bairro_mais_custoso(dicionario2):
    dica = total_do_semestre_por_bairro(dicionario2)
    chaves_lista = list(dica.keys)
    valores_lista = list(dica.values)
    return key[valores_lista.index(max(valores_lista))]
        
       
  
        