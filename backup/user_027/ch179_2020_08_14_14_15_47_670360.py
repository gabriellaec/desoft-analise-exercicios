def posicoes_minusculas(string:str):
    return [index for index,char in enumerate(string) if char.islower()]