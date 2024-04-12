from random import *

def psswd_gen(num, diff):
    alph_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = 'abcdefghijklmnopqrstuvwxyz'
    psswd = ''
    cpt_l = 0
    cpt_n = 0
    if diff == 'e':
        for i in range(num):
            psswd += str(randint(0, 100))
    elif diff == 'm':
        for i in range(num):
            r = randint(0, 1)
            if cpt_l >= num//2:
                r = 1
            elif cpt_n >= num//2:
                r = 0
            
            if r == 0:
                r = randint(0, 1)
                if r == 0:
                    psswd += alph_upp[randint(0, 25)]
                else:
                    psswd += alph_low[randint(0, 25)]
                cpt_l += 1
            else:
                psswd += str(randint(0, 100))
                cpt_n += 1
    

    return psswd

a = int(input(""))
print(psswd_gen(a, 'm'))