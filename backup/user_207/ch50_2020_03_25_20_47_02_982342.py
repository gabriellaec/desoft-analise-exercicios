nome =['Guilherme', 'Augusto', 'Fernando', 'Ivan']
sobrenome =['Rosada', 'Abc', 'DEF', 'GHI']
nome_e_sobrenome = []

def junta_nome_sobrenome(nome, sobrenome):
    i=0
    while i<len(nome):
        nome_e_sobrenome.append(nome[i] + ' ' + sobrenome[i])
        i += 1
    return nome_e_sobrenome

print (junta_nome_sobrenome(nome,sobrenome))
