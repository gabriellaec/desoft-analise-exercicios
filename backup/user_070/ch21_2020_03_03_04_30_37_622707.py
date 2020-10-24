D=input('Dias: ')
H=input('Horas: ')
M=input('Minutos: ')
S=input('Segundos: ')

d=int(D)
h=int(H)
m=int(M)
s=int(S)

x=s+(m*60)+(h*60*60)+(d*24*60*60)

print(x)