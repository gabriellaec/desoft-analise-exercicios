nome = ['joana', 'maria', 'carlos', 'antonio']
sobrenome = ['pereira', 'moura', 'santos', 'paiva']

def junta_nome_sobrenome(nomes, sobrenomes):
    nome_completo = [0]*len(nomes)
    i = 0
    while i < len(nomes):
        nome_completo[i] = nomes[i] + ' ' + sobrenomes[i]
        i += 1
    return nome_completo

print(junta_nome_sobrenome(nome, sobrenome, espaço))