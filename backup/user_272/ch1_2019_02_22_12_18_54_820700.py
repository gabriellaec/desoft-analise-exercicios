#FV=PV*((1+i)**N)
#valor futuro FV
#valor presente PV
#taxa de juros i=1,5%/mês
#tempo de aplicação n 

def calcula_valor_devido(PV,i,N):
    FV=PV*((i+1)**N)
    return FV
PV=1000
i=0.015
N=12
print(calcula_valor_devido(PV,i,N))