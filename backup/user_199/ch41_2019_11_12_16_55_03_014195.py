senha=input('digite a senha: ')
i=0
while senha!='desisto':
    senha=input('Senha incorreta, tente novamente: ')
    i+=1
if senha == 'desisto':
    print('Voçe acertou a senha!')