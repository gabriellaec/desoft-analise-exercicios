def remove_vogais(texto):
    texto_consoantes=""
    for letra in texto:
        if letra not in texto:
            texto_consoantes += letra
    return texto_consoantes


        
      