from operator import invert
import random as rn
import re

#Sentences builders
def sorting_hat(items):
    The_Choosen_One = rn.choice(items)
    return The_Choosen_One

def sentence_starter():
    inventory = ['Primero ve a la cinta','Busca la cinta','Dirigete a la cinta','Selecciona la cinta']
    return sorting_hat(inventory)

def second():
    inventory = ['ve al grupo','busca el grupo','dirigete al grupo','selecciona el grupo']
    return sorting_hat(inventory)


def conncetors():
    inventory = ['de ahi vas a','busca','selecciona','elige','escoge']
    return sorting_hat(inventory)

def more_conncectors():
    inventory = ['y','entonces','luego','ahora']
    return sorting_hat(inventory)

#Others
def is_bigger(old,new):
    if new > old:
        return True
    else:
        return False

#if have more options return True
def more_options(group):
    if type(group) == dict:
        return True
    else:
        return False