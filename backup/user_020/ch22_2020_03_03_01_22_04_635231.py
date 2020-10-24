def expectativa_de_vida(n, t):
    f = ((365*n)*t)/(86400)
    return f
n = int(input('Insira o número de cigarros que você fuma por dia: '))
t = int(input('Insira há quantos anos você fuma cigarros: '))
z = expectativa_de_vida(n,t)
print(z)