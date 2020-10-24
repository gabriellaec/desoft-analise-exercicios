def calcula_media(alunos):
    total = 0
    quant = 0
    for i in alunos:
        values = i.values()
        quant += len(values)
        total += sum(values)
    return total/quant