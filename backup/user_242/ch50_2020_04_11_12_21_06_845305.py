nome = ['Letícia ', 'Rafael ', 'Carolina ', 'Lais ']
sobrenome = ['Sanchez', 'Garcia','Moretti', 'Ferré']
nome_sobrenome=[]
i=0
def junta_nome_sobrenome(nome,sobrenome):
    if nome[i]==sobrenome[i]:
        nome_sobrenome.append(nome[i], sobrenome[i])
        print(nome_sobrenome)
    else:
        print('Não compatível')


