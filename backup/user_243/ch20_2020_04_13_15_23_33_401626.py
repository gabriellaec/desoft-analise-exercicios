a=float(input("Quantos km deseja percorrer?"))
if a<200:
    preço=a*0.5
    real=round(preço/2)
    print(real)
else:
    preço2=100+(a-200)*0.45
    real=round(preço2/2)
    print(real)