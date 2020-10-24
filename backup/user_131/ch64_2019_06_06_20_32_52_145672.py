def nome_uruario(email):
    for e in len(email):
        if email[e] == '@':
            return email[ : e]
