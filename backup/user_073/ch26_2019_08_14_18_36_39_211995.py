def tempo_em_segundos(n1,n2):
    tempo=(n1*(60)**2)+(n2*60)
    return tempo
n1=int(input('horas'))
n2=int(input('minutos'))
print(tempo_em_segundos(n1,n2))