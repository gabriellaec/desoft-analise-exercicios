import random
print('Você possui 100 reais.')
dinheiro=100
valor_aposta = input("Quantos reais você quer apostar? ")
i= (valor_aposta != "0" or "zero")
i = True
while i:
    questao = input('A aposta será em número(n) ou paridade(p)? ')
    if questao == 'n':
        digite = input("Digite um número de 1 a 36: ")
        sorteio = random.randint(0,36)
        if sorteio == digite:
			dinheiro= 100+(valor_aposta*35)
            print=('Parabéns, você tem {0} reais agora'.format(valor_aposta))
		else:
            dinheiro= 100-valor_aposta
	elif questao == 'p':
        escolha_par_impar=input('EScolha par(p) ou ímpar(i): ')
        sorteio_par_impar=random.randint(p,i)
else:
    print('Fim')
            
        