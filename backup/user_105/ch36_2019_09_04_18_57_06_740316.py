numero = int(input('diga um numero'))
divisor=2
	if numero==2:
        print('primo')
	elif numero==1:
        print('nao é primo')
    elif numero==0:
        print('nao é primo')
    else:
        if numero%2==0:
            print('nao é primo')
		elif numero%2!=0:
            while((divisor+2)<numero):
                if numero%divisor==0:
                    print('nao é primo')
                    break
                divisor=divisor+1
            else:
                	print('primo')
             