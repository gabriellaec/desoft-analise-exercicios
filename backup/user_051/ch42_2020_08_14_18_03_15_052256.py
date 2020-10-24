X=input('Palavra: ')
Lista=[]
while X!='fim':
    Lista.append(X)
    X=input('palavra: ')
for i in Lista:
    if i[0]=='a' or i[0]=='A':
        print(i)