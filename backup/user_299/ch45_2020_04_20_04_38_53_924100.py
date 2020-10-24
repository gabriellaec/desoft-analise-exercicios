num = int(input("digite um número:"))
listadenum = []
listadenum.append(num)
while num > 0:
    num = int(input("digite um número:"))
    listadenum.append(num)
listainvertida = [0]*len(listadenum)
for i,e in enumerate(listadenum):
    listainvertida[-i] = e
listainvertida.append(listainvertida[0])
del listainvertida[0]

print(listainvertida)
    
        

    