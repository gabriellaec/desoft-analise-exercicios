a = int(input('Qual o número?'))
S = 0

while a != 0:
    S = S + a
    a = int(input('Qual o número?'))
if a == 0:
    print(S)