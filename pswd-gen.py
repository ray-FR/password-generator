from random import *

alph_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_low = 'abcdefghijklmnopqrstuvwxyz'
spec_char = '!@#$%^&*()_+'


def psswd_gen(num, diff):
    psswd = ''
    cpt_l = 0
    cpt_n = 0
    cpt_s = 0
    if diff == 'e':
        for i in range(num):
            psswd += str(randint(0, 9))


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
                psswd += str(randint(0, 9))
                cpt_n += 1
    
    else:
        for i in range(num):
            r = randint(0, 2)
            if cpt_l >= num//2:
                r = 1
            elif cpt_n >= num//2:
                r = 0
            elif cpt_s >= num//2:
                r = randint(0, 1) #this is horrible
            
            if r == 0:
                r = randint(0, 1)
                if r == 0:
                    psswd += alph_upp[randint(0, 25)]
                else:
                    psswd += alph_low[randint(0, 25)]
                cpt_l += 1
            elif r == 1:
                
                psswd += str(randint(0, 9))
            else:
                psswd += spec_char[randint(0, 11)]

    return psswd

a = int(input("Number of characters in password?\n"))
diff = str(input("Difficulty level? (e, m or leave blank for hard difficulty.)\n"))
while diff not in ["e", "m", ""]: diff = str(input("Error, character not recognised, please re-enter character. \n")) 
print(psswd_gen(a, diff))