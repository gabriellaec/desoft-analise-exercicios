'''
21. Total em segundos
Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário. 
Depois calcule o total em segundos e imprima.
'''
dias = int(input("Quantos dias? "))
horas = int(input("Quantas horas? "))
minutos = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))
total = (dias * 86400) + (horas * 3600) + (minutos*60) + (segundos)
print(total)