distancia = float(input("Insira a distancia que pretende viajar: "))
if distancia <= 200:
    print(f"Preço da viagem é igual a R${distancia*0.5:.2f}")
else:
   	print(f"Preço da viagem é igual a R${100+((distancia-200)*0.45):.2f}")