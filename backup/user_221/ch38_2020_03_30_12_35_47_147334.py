def quantos_uns(x):
    i = 0
    contador = 0
while contador <= len(x):
        if x[i] == 1:
            cont += 1
            i +=1
        else:
            i += 1
print ('existe {} uns'.format(contador))