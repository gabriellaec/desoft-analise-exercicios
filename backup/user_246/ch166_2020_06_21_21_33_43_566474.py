def total_do_semestre_por_bairro(bairros):
    soma = {}
    for b in bairros:
        total = 0
        bairro = bairros[b]
        bairro = bairro[6:]
        for custo in bairro:
            total += custo
        soma[b] = total
    return soma
            
            
        