import unicodedata
import string

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

palav = ''
lista_palavras = []
ocor_bana = 0

f= open("macacos-me-mordam.txt","r")


conteudo = f.read()
for letra in conteudo:
    letra = normalize_caseless(letra)

    if letra not in list(string.punctuation) and letra != ' ':
        palav += letra

    else:
        palav = normalize_caseless(palav)
        lista_palavras.append(palav)
        palav = ''

for palavra in lista_palavras:
    if palavra == 'banana':
        ocor_bana+=1

print(ocor_bana)