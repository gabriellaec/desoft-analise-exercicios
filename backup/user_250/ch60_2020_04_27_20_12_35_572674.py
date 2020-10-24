def eh_palindormo(palavra):
    for i in palavra:
        if palavra[i] == palavra[:-i]:
            return True
        else:
            return False