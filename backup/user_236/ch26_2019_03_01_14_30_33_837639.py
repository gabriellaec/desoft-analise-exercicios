D=int(input("Qunatos dias? "))
H=int(input("Quantas horas? "))
M=int(input("Qunantos minuntos? "))
S=int(input("Quantos segundos? "))
T=((24*D+H)*60+M)*60+S
print(tempo(D,H,M,S))