from string import ascii_lowercase
from collections import Counter

with open("palavras.txt") as f:
    print(Counter(letra for line in f 
                  for letra in line.lower() 
                  if letra in ascii_lowercase))
#esse programa conta todas as palavras, e consequentemente a letra "A" e "a"também