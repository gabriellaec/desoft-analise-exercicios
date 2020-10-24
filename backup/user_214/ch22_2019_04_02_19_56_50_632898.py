ano=int(input("Qual ano você deseja? "))

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print("False")
    else:
        print("True")