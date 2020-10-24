pergunta_velocidade=int(input('Qual a sua velocidade em km/h?' ))
if pergunta_velocidade>80:
    print('Você foi multado')
    def funcao_multa:
        multa = 5*(pergunta_velocidade - 80)
        print('sua multa é de {0.2f}'.format(multa))
else:
    print('Não foi multado')