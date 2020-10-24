with open('texto.txt', 'r') as arq:
    cont = arq.read()
word = cont.split()
print(len(word))