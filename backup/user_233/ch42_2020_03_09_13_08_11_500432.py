palavras = []

while True:
    palavra = input()
    palavras.append(palavra)
    if palavra == 'fim': break

for palavra in palavras:
    if palavra[0] == 'a': print(palavra)