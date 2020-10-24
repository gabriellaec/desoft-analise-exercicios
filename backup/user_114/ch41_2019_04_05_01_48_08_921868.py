def pergunta(palavra):
    senha=False
    while senha:
        palavra=input('tentativa senha: ')
        if palavra=='desisto':
            senha=True
            return 'Você acertou a senha'
        else:
            return False