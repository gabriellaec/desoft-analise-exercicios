deposito_inicial=float(input('qual é o seu depósito inicial?   :'))
taxa_de_juros=float(input('e a taxa de juros?  :'))
i=0
while i<=24:
    y=deposito_inicial*((1+taxa_de_juros)**i)
    x=round(y,2)
    print (x)
    i+=1
print(x-deposito_inicial)
    