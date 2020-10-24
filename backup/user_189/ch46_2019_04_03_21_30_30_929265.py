a=[]
i=0
palavra=str(input('digite uma palavra: '))
while palavra!='fim':
    a.append(palavra)   
    palavra=str(input('digite uma palavra: '))         
while i<len(a):
	palavra=a[i]
    if a[i][0]=='a':
		print(palavra)
	i+=1
                          