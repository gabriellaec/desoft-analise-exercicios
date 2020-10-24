def tempo_de_vida(n,x):
    f = ((n*365)*(x)*(10)/1440)
    return f
n = int(input('quantos cigarros por dia você fuma?'))
x = int(input('À quanto tempo você fuma em anos?'))
w = tempo_de_vida(n,x)
print(w)
