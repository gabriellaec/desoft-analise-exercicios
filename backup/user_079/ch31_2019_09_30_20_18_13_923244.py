x=int(input("casa?: "))
y=int(input("salario?: "))
z=int(input("meses?: "))
conta = x/z
if conta >= (y*0.3):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
