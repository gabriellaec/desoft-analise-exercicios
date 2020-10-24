duvida = True
while duvida:
    x = str(input("Você tem dúvidas? "))
    if x != 'não':
        print ('Pratique mais')
    if x == 'não':
        print("Até a próxima")
        duvida = False