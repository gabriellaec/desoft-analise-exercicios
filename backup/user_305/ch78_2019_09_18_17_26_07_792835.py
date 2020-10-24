a = input("Nome do atleta")
b = int(input("aceleração"))
dic = {}
dic2 = {}
while a != "sair":
    dic[a] = b
    a = input("Nome do atleta")
    b = int(input("aceleração"))

menortempo = -1
menorkey = ""
for k,v in dic.items():
	tempo = (200/v)**(1/2)
	dic2[k] = tempo
    if menortempo == -1 or tempo < menortempo:
        menortempo = tempo
        menorkey = k
print("O vencedor é" k" com tempo de conclusão de "menortempo) 