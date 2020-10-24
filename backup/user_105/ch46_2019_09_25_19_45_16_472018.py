palavras = []
palavras_sem_a:[]
palavra = input('diga uma palavra')
palavras.append(palavra)
i = 0
palavras.append(palavra)
while palavra !='fim':
	palavra = input('diga uma palavra')
	palavras.append(palavra)
	if palavra[0]=='a':
		palavras.append(palavra)
	
    
