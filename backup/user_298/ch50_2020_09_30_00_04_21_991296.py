nome = []
sobrenome = []
nomes_completos = []
def junta_nome_sobrenome(nome,sobrenome):
    t = 0    
    while t < len(nome):
        completo = nome[t] + "" + sobrenome[t]
        nomes_completos.append(completo)
        t += 1
    return print(nomes_completos)