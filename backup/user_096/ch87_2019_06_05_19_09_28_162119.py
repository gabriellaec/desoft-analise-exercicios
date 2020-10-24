# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:03:07 2019

@author: felip
"""
'''
def libras_para_kg(libras):
    kg=libras/2.204623
    return format(kg,'.6f')
print(libras_para_kg(1))
'''
'''
p = 9
def somatoria(p):
    i=1
    s=0
    while i<=p:
        s+=i**3
        i+=1
    return s



def expressao(n):
    y=(n*(n+1)/2)**2
    return y




def comparacao(x):
    k=0
    while k<=x:
        if somatoria(k)==expressao(k):
            print('coincidiu para o valor {0}'.format(k))
        else:
            print('não coincidiu para o valor {0}'.format(k))
        k+=1
            
print(comparacao(p))


import math

g=9.8
def calcula_distancia_do_projetil(g,theta,v,y0):
    a=(v**2)/2*g
    b=math.sin(2*theta)
    c=math.sqrt(1+((2*g*y0)/(v**2)*math.sin(theta)**2))
    d=a*(1+c)*b
    return d

'''

'''

def verifica_idade(idade):
    if idade>21:
        return"Liberado EUA e BRASIL"
    elif 18<idade<21:
        return"Liberado BRASIL"
    elif idade<18:
        return"Não está liberado"
        
'''
'''
def eh_bissexto(ano):
    if ano%4==0 and ano!=100:
        return True and print('rola')
    else:
        return False
    


print(4%4)
'''
'''
import math
F=10
r=2
def pressao(F,r):
    P=F/(math.pi*r**2)
    return P
print(pressao(F,r))
'''
'''
psis=int(input('qual sua pressão sistólica: '))
pdis=int(input('qual sua pressão diastólica: '))

if psis<120  and pdis<80:
    print('pressão Normal')
elif 120<psis<130 and 80>pdis:
    print('Pressão Elevada')
elif 130<psis<140 or 80<pdis<90:
    print('Hipertensão estágio 1')
elif 140<psis<181 or 90<pdis<121:
    print('Hipertensão estágio 2')
elif psis>180 or pdis>120:
    print('Crise hipertensiva')
'''

'''
def log_merda(x,b):
    i=1
    v=x/b
    while v>=b:
        v=v/b
        i+=1
    return i
print(log_merda(16,2))
'''
'''
n1=int(input('manda um numero positivo: '))
n2=int(input('manda um numero positivo: '))
def simplifica(n1,n2):
    i=1
    e=1
    if n1>n2:
        while n1%i==0 and n2%i==0:
            i+=1
        a=print('simplifacado fica {1}/{0}'.format(n1/i,n2/i))
        return a
    if n1<n2:
        while n1%e==0 and n2%e==0:
            e+=1
        else:
            b=print('simplifacado fica {0}/{1}'.format(n1/e,n2/e))
            return b
print(simplifica(n1,n2))

'''
'''
i=2
e=3
a=int(input('fa: '))
b=int(input('fa: '))
print('simplifacado fica {0}/{1}'.format(a*i,b*e))
'''
'''
nomes=input('qual o numero do mes: ')

if nomes == 'janeiro':
    print(1)
elif nomes == 'fevereiro':
    print(2)
elif nomes == 'março':
    print(3)
elif nomes == 'abril':
    print(4)
elif nomes == 'maio':
    print(5)
elif nomes == 'junho':
    print(6)
elif nomes == 'julho':
    print(7)
elif nomes == 'agosto':
    print(8)
elif nomes == 'setembro':
    print(9)
elif nomes == 'outubro':
    print(10)
elif nomes == 'novembro':
    print(11)
elif nomes == 'dezembro':
    print(12)
'''
'''
string='araraquara'
def requebra(string):
    contador = 0
    x = string.split(' ')
    for i in range(len(x)):
        for e in x[i-1]:
            if e == "a":
                contador +=  1
    return contador

print(requebra(string))
'''
'''
email='felpinhoplays@gmail.com'
def arroba(email):
    i = 0
    for i in range(len(email)-1):
        if email[i] == "@" and i < (len(email)-1):
            return email[:i]
print(arroba(email))
'''
'''
lista = range(0,11)
for e in lista:
    print(e)
''' 
'''
lista=[]
for i in range(10):
    lista.append(int(input('fala um valor: ')))
print(max(lista))
'''
'''
s=0
for e in lista:
    s+=e
print(s)
'''
'''
listaa=['couve','tomate','couve','couve','tomate','tomate','tomate']
def listap(lista):
    dicionario={}
    for e in lista:
        if e in dicionario:
            dicionario[e]+=1
        else:
            dicionario[e]=1
    return dicionario


def palavra_freq(lista):
    dicionario = listap(listaa)
    valores = dicionario.values()
    maior = max(valores)
    for k in dicionario:
        if dicionario[k] == maior:
            return k,maior
    

print(palavra_freq(listaa)) 
'''
'''
def calcula_aumento(salario):
    if salario>1250:
        return salario*1.1
    elif salario<=1250:
        return salario*1.15
    
print(calcula_aumento(1250))
'''
'''
palavra = input('fale uma palavra: ')
palavra_a = []
while palavra != 'fim':
    if palavra[0] == 'a':
        palavra_a.append(palavra)
        palavra = input('fale uma palavra: ')
        print(palavra_a)
    else:
        palavra = input('fale uma palavra: ')
print(palavra_a)
'''
'''
numeros = int(input('digite um numero: '))
numerosd = []
while True:
    if numeros > 0:
        numerosd.append(numeros)
        numeros = int(input('digite um numero: '))
    elif numeros <= 0:
        print(numerosd[::-1])
        break
'''
'''
lista = [0,1,3,3,2,5]
def numero_no_indice(lista):
    listaa = []    
    for i in range(len(lista)):
        if i == lista[i]:
            listaa.append(lista[i])
    return listaa
print(numero_no_indice(lista))
'''
'''
casa = float(input('qual o valor da casa: '))
salario = float(input('qual o salario: '))
anos = float(input('quantos anos ate pagar: '))*12
prestacao = casa/anos
salario30 = salario*0.3
if prestacao > salario30:
    print('Empréstimo não aprovado')
elif salario30 > prestacao:
    print('Empréstimo aprov410ado')
'''
'''
lista = [1,2,3,4,5,6,7,8,9]
def inverte_lista(lista):
    return lista[::-1]
print(inverte_lista(lista))
'''
'''
nome = ['Luiz','Andre','Katia','Manuel']
sobrenome = ['Valente','Domingues','Branco','Neto']

def junta_nome_sobrenome(nome,sobrenome):
    listaa = []
    i = 0
    while i < len(nome) and i < len(sobrenome):
        listaa.append(nome[i] + ' ' + sobrenome[i])
        i+=1
    return listaa
print(junta_nome_sobrenome(nome,sobrenome))
'''
'''
import math

def calcula_norma(vetor):
    soma = 0
    for e in vetor:
        soma+=e**2
    return math.sqrt(soma)
print(calcula_norma(vetor))
'''
'''
string = 'banana nanica'
def conta_bigramas(string):
    lista = []
    saida = {}
    i=0
    while i<len(string)-1:
        lista.append(string[i]+string[i+1])
        i+=1
    for e in lista:
        if e not in saida:
            saida[e] = 1
        elif e in saida:
            saida[e] += 1
    return saida
print(conta_bigramas(string))
'''
'''
def primos(p):
    i=0
    if p==1:
        return False
    while p>0:
        for y in range(1,p+1):
            if p%y==0:
                i+=1
        if i<=2:
            return True
        else:
            return False
lista = [1,2,3,4,5,56,852,6,854,68,11,13,15,23,47]
def verifica_primos(lista):
    saida = {}
    for e in lista:
        if primos(e) == True:
            saida[e] = 1
        elif primos(e) == False:
            saida[e] = 0
    return saida
print(verifica_primos(lista))
'''
'''
string = 'laranjeiras'
def lista_caracteres(string):
    lista = []
    for e in string:
        if e not in lista:
            lista.append(e)
    return lista
print(lista_caracteres(string))
'''
'''
n = 50
def asteriscos(n):
    a = '*'*n
    return a
print(asteriscos(n))
'''
'''
lista = [1,-2,-3,4,-5,6]
def filtra_positivos(lista):
    listap = []
    for e in lista:
        if e > 0:
            listap.append(e)
    return listap
print(filtra_positivos(lista))
'''
'''
lista = [1,2,5,3,6,4,7]
def estritamente_crescente(lista):
    i = 1
    listac = []
    if len(lista) == 0:
        return []
    listac.append(lista[0])
    maior = lista[0]
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
            listac.append(lista[i])
            i+=1
        else:
            i+=1
    return listac
print(estritamente_crescente(lista))
'''
'''
lista= [1,1,3,3,6,7]
def eh_crescente(lista):
    i = 1
    listac = []
    if len(lista) == 0:
        return False
    listac.append(lista[0])
    maior = lista[0]
    while i < len(lista):
        if lista[i] >= maior:
            maior = lista[i]
            listac.append(lista[i])
            i+=1
        else:
            i+=1
    if lista == listac:
        return True
    else:
        return False
print(eh_crescente(lista))
'''
'''
dicionario = {'jake':'23/12/1996','jaks':'23/09/1996','jakas':'23/10/1996','jaake':'23/09/1996'}
def aniversariantes_de_setembro(dicionario):
    saida = {}
    for nome,data in dicionario.items():
        if data[4] == '9':
                saida[nome] = data
    return saida
print(aniversariantes_de_setembro(dicionario))
'''
'''
import math
dicionario = {}
while True:
    nome = input('qual o nome: ')
    if nome != 'sair':
        aceleracao = float(input('qual a aceleracao: '))
        dicionario[nome] = aceleracao
    elif nome == 'sair':
        break
def calcula_tempo(dicionario):
    saida = {}
    for atleta,a in dicionario.items():
        saida[atleta] = math.sqrt(200/a)
    return saida
saida = {'joe':2,'robertp':3,'felps':1}
def vencedor(saida):
    for k,v in saida.items():
        
print(vencedor(saida))
'''
'''
lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [9,8,7,6,5,4,3,2,1]
def monta_dicionario(lista1, lista2):
    saida = {}
    i = 0
    while i < len(lista2):   
        for e in lista1:
            saida[e] = lista2[i]
            i+=1
    return saida
print(monta_dicionario(lista1,lista2))
'''
'''
dicionario1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dicionario2 = {'A': 5, 'B': 6, 'C': 7, 'E': 8}
def interseccao_chaves(dicionario1,dicionario2):
    listac = []
    for k1 in dicionario1.keys():
        for k2 in dicionario2.keys():
            if k1 == k2:
                listac.append(k1)
    return listac
print(interseccao_chaves(dicionario1,dicionario2))

def interseccao_valores(dicionario1,dicionario2):
    listac = []
    for v1 in dicionario1.values():
        for v2 in dicionario2.values():
            if v1 == v2:
                listac.append(v1)
    return listac
'''
'''
email = 'usuario@insper.edu.br'
def pos_arroba(email):
    i=0
    while True:
        if email[i] != '@':
            i += 1
        elif email[i] == '@':
            return i + 1
            break
        
'''
'''
email = 'usuario@insper.edu.br' 
def nome_usuario(email):
    i=0
    while True:
        if email[i] != '@':
            i += 1
        elif email[i] == '@':
            return email[:i:1]
            break
print(nome_usuario(email))
'''
'''
lista = [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]]
def junta_listas(lista):
    listac = []
    for e in lista:
        listac.append(e)
    return listac
print(junta_listas(lista))
'''
'''
with open('arquivo.csv','r') as arquivo:
    conteudo = arquivo.read()
palavras = conteudo.split(',')
conteudo = '\t'.join(palavras)
print(conteudo)
'''
'''
def inverte_dicionario(dicionario):
    saida = {}
    lista_idades = []
    for k,v in dicionario.items():
        for v in dicionario.values():
            lista_idades.append(v)
            
    return saida
'''
'''
numero = 10015423
def quantos_uns(numero):
    numero = str(numero)
    uns = 0
    for i in numero:
        if i == '1':
            uns += 1
    return uns

print(quantos_uns(numero))
'''
'''
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.lower()
    a = a.split()
    i = 0
    for e in a:
        if e == 'banana':
            i += 1
print(i)
'''
'''
import csv
with open('dados.csv','r') as csvin, open('dados.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)
'''
a = []
with open('churras.txt', 'r') as arquivo:
    churras = arquivo.read()
    lista = churras.split() and churras.split('\n')    
    gasto = 0
    for e in lista:
        a.append(e.split(','))
    for item in a:
        gasto += int(item[1])*float(item[2])            
print(gasto)

        
        



























