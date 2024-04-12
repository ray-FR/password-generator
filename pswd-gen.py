from random import *

def psswd_gen(num, diff):
    alph_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = 'abcdefghijklmnopqrstuvwxyz'
    psswd = ''
    if diff == 'easy':
        for i in range(num):
            psswd += str(randint(0, 100))

    return psswd

a = int(input(""))
print(psswd_gen(a, 'easy'))