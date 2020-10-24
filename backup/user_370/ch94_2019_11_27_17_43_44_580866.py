velocidade_max=float(input("Qual a velocidade maxima da via?"))
pergunta_distancia=float(input("Qual a distancia entre as cameras?"))

pergunta_placa=int(input("Qual a placa do veiculo"))

for i in len(pergunta_placa):
    if i == "7":
        pergunta_placa=int(input("Qual a placa do veiculo"))
        tempo=float(input("Qual o instante percorrido?"))
        velocidade= pergunta_distancia / tempo
        if velocidade > velocidade_max and velocidade <= velocidade_max * 0.2:
            print('Infracao Media, sua penalidade sera uma multa de R$130,16')
        elif velocidade> velocidade_max * 0.2 and velocidade <=velocidade_max * 0.5:
            print('Infracao Grave, sua penalidade sera uma multa de R$195,23')
        elif velocidade > velocidade_max * 0.5:
            print('Infracao Gravissima, sua penalidade sera: multa[tres vezes](3x R$195,23)+ suspensão imediata do direito de dirigir e apreensão do documento de habilitação.')
        else:
            print('Voce nao obteve infracoes, obrigada')
    else :
        break
