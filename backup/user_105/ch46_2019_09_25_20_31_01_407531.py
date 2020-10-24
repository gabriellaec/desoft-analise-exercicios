palavras = []
palavras_sem_a=[]
palavra = input('diga uma palavra: ')
palavras.append(palavra)
if palavra[0]== 'a':
	palavras_sem_a.append(palavra)
while palavra !='fim':
	palavra = input('diga uma palavra: ')
    palavras.append(palavra)
	
	if palavra[0]=='a':
		palavras_sem_a.append(palavra)
print(palavras_sem_a)
	
