def eh_palindormo(string):
    if string[::] == string[::-1]:
        return True
    else:
        return False