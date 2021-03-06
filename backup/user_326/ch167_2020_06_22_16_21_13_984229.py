def total_do_semestre_por_bairro(dic_bairros):
    valor_gasto_semestre = {}
    for bairro, valores in dic_bairros.items():
        total_gasto = 0
        valores = valores[::-1]
        for i in range(6):
            total_gasto += valores[i]
        valor_gasto_semestre[bairro] = total_gasto
    return valor_gasto_semestre

def bairro_mais_custoso(dic_bairros):
    maior_custo = 0
    bairro_mais_caro = ''
    for bairro, valor in dic_bairros:
        if valor > maior_custo:
            maior_custo = valor
            bairro_mais_caro = bairro
    return bairro_mais_caro