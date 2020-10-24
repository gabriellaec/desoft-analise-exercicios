lista = []
i = 0
a = input('Palavra:   ')
while a != 'fim':
       a = input('Palavra:   ')
       lista.append(a)
       while i < len(lista):
           if lista[i][1] == 'a':
               print(lista[i])
               i += 1
           else:
               i += 1