def nome_usuario (e_mail):
    def pos_arroba(e_mail):
        palavra = 'e_mail'
        resposta = palavra.find('@')
        return resposta
    
    nome_do_usuario = palavra[0:resposta]
    return nome_do_usuario