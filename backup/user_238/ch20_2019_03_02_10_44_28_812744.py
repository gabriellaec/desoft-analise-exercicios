def odeio_chris(nome):
        if (nome)  ==  str('chris'):
            resposta='Todo mundo odeia o Chris'
        else:
            resposta='olá, '+str(nome)
        return resposta
(nome)=str(input('escreva seu nome: '))
print(odeio_chris(nome))