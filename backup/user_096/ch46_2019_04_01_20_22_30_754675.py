palavra = input('fale uma palavra: ')
palavra_a = []
while palavra != 'fim':
    if palavra[0] == 'a':
        palavra_a.append(palavra)
        palavra = input('fale uma palavra: ')
        print(palavra_a)
    else:
        palavra = input('fale uma palavra: ')
print(palavra_a)
