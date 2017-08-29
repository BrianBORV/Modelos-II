'''
Created on 29/08/2017

@author: Estudiantes
'''
from random import*

def mazo():
    return sample([(x,y) for x in ['A','J','Q','K'] + list(range(2,11)) for y in ['picas','treboles','diamantes','corazones']], 52)

def jugar(mazo):
    if mazo!=[]:
        print(mazo[0])
        print(mazo[1])
        return jugar (mazo[2:])
        
jugar(mazo())