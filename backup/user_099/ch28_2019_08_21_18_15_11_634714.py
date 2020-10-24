def velocidade(v):
    if v>=80:
        return 'Você foi multado em R$ {0:.2f}'.format((v-80)*5)
    else:
        return 'Não foi multado'
    
v=float(input("Qual sua velocidade? "))
print(velocidade(v))