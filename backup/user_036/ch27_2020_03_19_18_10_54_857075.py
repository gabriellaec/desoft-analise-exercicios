duvida=True
a= input('Tem duvidas? ')
if a=='não':
    duvida=False
while duvida==True:
    print('Pratique mais')
    a= input('Tem duvidas? ')
    if a == 'não':
        duvida=False
        print('Até a proxima')