def velocidade(kmh):
    if kmh>80:
        return "Voce foi multado em: {0} ".format((kmh-80)*5)

    else:
        return "Não foi multado"
