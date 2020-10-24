 from math import *
def calcula_tempo (dic):
    dicl={}
    for e in dic:
        dicl[e]=sqrt(200/dic[e])
    return dicl
    