v = float(input("Qual a velocidade?"))

if float(v > 80):
    print("Foi multado.")
    print("Multa:")
    print(int( (v-80)*5))

if float (v <= 80):
    print("Não foi multado")
