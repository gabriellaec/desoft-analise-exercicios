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
    for chaves,gastos in dica.items():
       
        return max(chaves, dica.get())
        