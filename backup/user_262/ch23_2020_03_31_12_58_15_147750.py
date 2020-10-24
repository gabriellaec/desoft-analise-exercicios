mul=0
vel=int(input("informe a velocidade: "))
if vel>80:
    mul=(vel-80)*5
    return(mul)
else:
    print('Não foi multado')