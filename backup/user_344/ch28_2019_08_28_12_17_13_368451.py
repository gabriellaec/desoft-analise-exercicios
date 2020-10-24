v= int(input("qual velocidade?"))
if v > 80:
    multa= 5*(v-80)
    print('A multa foi de {:.2f}'.format(multa))
else:
    print('Não foi multado')
