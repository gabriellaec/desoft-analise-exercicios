p = []
p = input('Insira uma lista de palavras ')
while p != 'fim':
    p.append(palavra)
    palavra = input('Insira uma lista de palavras ')
i = 0
while i < 2:
    p = p[i]
    if p[0] == 'a' or p[0] == 'A':
	i += 1 
print(p)
   