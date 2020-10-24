def calcula_tempo(acel):
    tempo={}
    for corredor,aceleracao in acel.items():
        vf=(2*aceleracao*100)**(1/2)
        t=vf/aceleracao
        tempo[corredor]=t
    return tempo

    