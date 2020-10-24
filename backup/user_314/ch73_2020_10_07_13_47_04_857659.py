def remove_vogais (str):

    lista_v=['a','e','i','o','u']
    str1=''

    for i in str:
        if not (i in lista_v):
            str1+=i
    
    return str1