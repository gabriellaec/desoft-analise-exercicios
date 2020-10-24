def total_do_semestre_por_bairro(bairros):
    soma = {}
    for b in bairros:
        total = 0
        bairro = bairros[b]
        bairro = bairro[5:]
        for custo in bairro:
            total += custo
        total[b] = total
    return soma
            
            
        