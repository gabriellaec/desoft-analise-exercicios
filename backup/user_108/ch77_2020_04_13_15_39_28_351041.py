def calcula_tempo(acels):
    return {nome : (200/acels[nome])**(1/2) for nome in acels}