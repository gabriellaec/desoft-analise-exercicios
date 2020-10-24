def funcao_multa(pergunta_velocidade):
    if pergunta_velocidade<=80:
        return 'Não foi multado'
    elif pergunta_velocidade>80:
        multa = 5*(pergunta_velocidade - 80)
        return 'você foi multado em {0:.2f} reais'.format(multa)
        
pergunta_velocidade = float(input('Qual a sua velocidade em km/h?' ))
print(funcao_multa(pergunta_velocidade))


    