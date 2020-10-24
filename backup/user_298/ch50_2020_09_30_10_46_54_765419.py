
def junta_nome_sobrenome(nome,sobrenome):
    nomes_completos = []
    t = 0    
    while t < len(nome):
        completo = nome[t] + " " + sobrenome[t]
        nomes_completos.append(completo)
        t += 1
    return nomes_completos