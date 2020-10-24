def calcula_tempo(acels):
    return {nome : (200/acel[nome])**(1/2) for nome in acels}