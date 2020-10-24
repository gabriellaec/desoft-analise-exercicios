def nome_usuario(stg):
    y=stg.find('@')
    user=stg[:y]
    return user