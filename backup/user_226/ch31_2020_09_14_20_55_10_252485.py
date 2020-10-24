def eh_primo(numero):
    if numero % 2 != 0 and numero != 0 and numero != 1:
        if numero == 2 and numero == 3:
            return True
        else:
            i = 3
            while numero > i:
                if numero % i == 0:
                    print("não")
                    return False
                else:
                    i += 1
            if i >= numero:
                print("sim")
                return True
    else:
        print('não')
        return False