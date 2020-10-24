custo_total = 0
lin = []
with open('custo churrasco.txt','r') as arquivo:
    for linha in arquivo:
        lin.append(linha)

for n in range(0,len(lin)):
    lin[n] = lin[n].replace('\n','')
    lin[n] = lin[n].replace(' ','')
    lin[n] = lin[n].replace(',',' ')
    lin[n] = lin[n].split()

for v in lin:
    custo_total += int(v[1])*float(v[2])


print(custo_total) 