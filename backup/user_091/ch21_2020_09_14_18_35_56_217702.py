x=input("Escreva uma quantiade de dias ")
y=input("Escreva uma quantidade de horas ")
z=input("Escreva uma quantidade de minutos ")
w=input("Escreva uma quantidade de segundos ")

def converte_dias_horas_em_segundos(a):
    k=86400*a
    return k
def converte_horas_em_segundos(b):
    d=3600*b
    return d
def converte_minutos_em_segundos(c):
    j=60*c
    return j
def soma_em_segundos(l,o,p,q):
    m=l+o+p+q
    return m

print(soma_em_segundos(int(converte_dias_horas_em_segundos(x)),int(converte_horas_em_segundos(y)),int(converte_minutos_em_segundos(z)),int(w))))
    