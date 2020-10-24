x = int(input("quantos dias "))
y = int(input("quantas horas "))
z = int(input("quantos minutos "))
w = int(input("quantos segundos "))
def soma(dias,horas,minutos,segundos):
    d = 86400*dias
    h = 3600*horas
    m = 60*minutos
    s = segundos
    c = d+h+m+s
    return c
print(soma(x,y,z,w))