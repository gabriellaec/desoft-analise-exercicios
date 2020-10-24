game=True
palavra=[]
while game==True:
    p=input('qual palavra')
    if p==('fim'):
        game=False
    else:
        palavra.append(p)
for i in palavra:
    if i[1]==a:
        print(i)