with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
print(conteudo)
final = 0
for lista in conteudo:
    x = lista.split(',')
    print(x)
    quantidade = int(x[1])
    preco = float(x[2])
    total = quantidade*preco
    final += preco
print(final)