a = input("Nome do atleta")
b = float(input("aceleração"))
dic = {}
dic2 = {}
while a != "sair":
    dic[a] = b
    a = input("Nome do atleta")
    b = float(input("aceleração"))

menortempo = -1
menorkey = ""
for k,v in dic.items():
	tempo = (200/v)**(1/2)
	dic2[k] = tempo
	if menortempo == -1 or tempo < menortempo:
		menortempo = tempo
		menorkey = k
print("O vencedor é {0} com o tempo de conclusão de {1} s".format(k,menortempo)) 