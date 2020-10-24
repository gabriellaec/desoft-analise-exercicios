def d_h_m_s(d, h, m, s):
    Ts=d*86400+h*3600+m*60+s
    return Ts
    

a= int(input("Digite o número de dias: "))

Digite o número de dias: 5

b=int(input("Digite o número de horas: "))

Digite o número de horas: 12

c=int(input("Digite o número de minutos: "))

Digite o número de minutos: 6

e=int(input("Digite o número de segundos: "))

Digite o número de segundos: 30

z=d_h_m_s(a, b, c, e)

print(z)