v = int(input("Qual a velocidade?"))

if int(v > 80):
    print("Foi multado.")
    print("Multa:")
    print(int( (v-80)*5))

if int (v <= 80):
    print("Não foi multado.")
