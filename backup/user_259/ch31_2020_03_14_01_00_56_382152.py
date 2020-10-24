numero=int(input("Digite um número: "))
def eh_primo(numero):
	if numero%2==0 or numero%3==0 or numero%5==0 or numero%7==0:
    	if numero==2 or numero==3 or numero==5 or numero==7:
            return True
        else:
            return False
	else:
        return True
        
    