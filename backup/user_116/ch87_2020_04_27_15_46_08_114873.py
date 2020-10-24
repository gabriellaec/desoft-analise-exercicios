with open('churras.txt', 'r') as arquivo:
    ler=arquivo.readlines()
for ele in ler:
    ele.split(",")


print(ler)