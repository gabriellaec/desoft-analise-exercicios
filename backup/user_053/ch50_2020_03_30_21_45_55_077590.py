nome = ['joana', 'maria', 'carlos', 'antonio']
sobrenome = ['pereira', 'moura', 'santos', 'paiva']
espaço = ['']

def junta_nome_sobrenome(nomes, sobrenomes, espaco):
    nome_completo = [0]*len(nomes)
    espaco = ['']
    i = 0
    while i < len(nomes):
        nome_completo[i] = nomes[i] + espaço[0] + sobrenomes[i]
        i += 1
    return nome_completo

print(junta_nome_sobrenome(nome, sobrenome))