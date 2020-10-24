def tempo_em_segundos(n1,n2,n3,n4):
    tempo=((n1*(60)**2)*24)+(n2*60**2)+(n3*60)+n4
    return tempo
n1=int(input('dias'))
n2=int(input('horas'))
n3=int(input('minutos'))
n4=int(input('segundos'))
print(tempo_em_segundos(n1,n2,n3,n4))