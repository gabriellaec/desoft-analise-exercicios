def odeio_chris(nome):
        if nome == 'Chris':
            resposta='Todo mundo odeia o Chris'
        else:
            resposta='olá, ' + str(nome)
        return resposta
pessoa=input('escreva seu nome: ')
print(odeio_chris(pessoa))