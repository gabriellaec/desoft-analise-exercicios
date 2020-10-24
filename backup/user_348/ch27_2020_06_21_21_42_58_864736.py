# determina uma variável de estado
tem_duvidas = True

# determina a condição do loop (enquanto a variável de estado é True)
while tem_duvidas:
    # determina uma variável que faz a pergunta e armazena a resposta
    resposta = input('Alguma dúvida? (sim/não): ')
    # determina que enquanto a resposta for diferente de não, imprimirá 'Pratique mais' e voltará para o começo do loop
    if resposta != 'não':
        print('Pratique mais!')
    # muda o estado da variável de estado para False, interrompendo o loop
    else:
        tem_duvidas = False
# Quando sai do loop, imprime 'Até a próxima'
print('Até a próxima')