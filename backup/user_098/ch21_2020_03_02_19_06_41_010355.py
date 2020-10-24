qdias = float(input("Dias:"))
qhoras = float(input("Horas:"))
qminutos = float(input("Min:"))
qsegundos = float(input("Seg:"))

segundostotal = qdias*24*60*60 + qhoras*60*60 + qminutos*60 + qsegundos

print(segundostotal)