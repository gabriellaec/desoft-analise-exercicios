arquivo = open('palavras.txt', 'r')
data = arquivo.read()
arquivo.close()

data = data.split()

counter = 0
for i in range(len(data)):
    if data[i][:1] == 'a' or data[i][:1] == 'A':
        counter += 1

print('Existem {0} palavras que começam com "A" ou "a"'.format(counter))