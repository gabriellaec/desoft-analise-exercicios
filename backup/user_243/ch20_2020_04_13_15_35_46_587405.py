a=float(input("Quantos km deseja percorrer?"))
if a<=200:
    preço=a*0.5
else:
    preço=100+((a-200)*0.45)
print(f"{preço:.2f}")