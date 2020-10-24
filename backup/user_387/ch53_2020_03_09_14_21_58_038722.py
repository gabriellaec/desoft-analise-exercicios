def eh_impar(a):
    if a%2 == 0:
        return False

    else:
        return True


def soma_impares(a):

    total = 0

    for num in a:
        if eh_impar(num) == True:
            total+=num
    return total
 