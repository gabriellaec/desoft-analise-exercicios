from collections import Counter
with open("texto.txt", "r") as file:
    w=file.readlines()
x=",".join(w)
y=Counter(x)
print(y)
