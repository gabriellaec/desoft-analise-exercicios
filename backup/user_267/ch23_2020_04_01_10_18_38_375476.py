pergunta_velocidade=int(input('Qual a sua velocidade em km/h?' ))
if pergunta_velocidade>80:
    def funcao_multa(pergunta_velocidade):
        multa = 5*(pergunta_velocidade - 80)
        print('você foi multado em {0.2f} reais'.format(multa))
else:
    print('Não foi multado')