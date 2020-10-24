#dic1={atleta1:aceleração} muv deltas/deltat=a*deltat deltat=(deltas/acel)**1/2
#dic2={atleta1:tempo}
def calcula_tempo(dic1):
    dic2={}
    for i in dic1:
        deltat=(100/dic1[i])**(1/2)
        dic2[dic1[i]]=deltat
    return dic2