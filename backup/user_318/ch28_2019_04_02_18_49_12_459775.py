v=int(input("Qual é a velociade do carro?"))
if(v>80):
    s=(v-80)*5
    print("R$ {0:.2f}".format(s))
if(v<=80):
    print("Não foi multado")
    