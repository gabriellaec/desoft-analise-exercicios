inicial=float(input("Qual seu deposito inicial?"))
mensal=float(input("Qual seu deposito mensal?"))
taxajuros=input("Quanto é sua taxa de juros de uma poupança?")

print(inicial)

i=1
valorfinal=0
while i <24: 
    valorfinal=valorfinal(1+i)**23
    i+=1
    print (i)