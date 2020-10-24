def tempo(D,H,M,S):
    T=((24*D+H)*60+M)*60+S
    return T
D=int(input("Qunatos dias? "))
H=int(input("Quantas horas? "))
M=int(input("Qunantos minuntos? "))
S=int(input("Quantos segundos? "))
print(T)