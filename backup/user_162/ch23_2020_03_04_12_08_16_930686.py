v = int(input("Qual sua velocidade: "))
if v <= 80: 
    print("Não foi multado")
else:
    vtaxa = (v-80)*5
    print("Voce deve {:.2f}".format(vtaxa))
    