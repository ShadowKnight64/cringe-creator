# CRINGE CREATOR V 1.0

import random

class fgnames:
    n0 = "Akane"
    n1 = "Hana"
    n2 = "Hiruka"
    n3 = "Hikari"
    n4 = "Riley"
    n5 = "Yumi"
    n6 = "Nori"
    n7 = "Atsuko"

class fbnames:
    n0 = "Alex"
    n1 = "Fumio"
    n2 = "Kenta"
    n3 = "Sasuke"
    n4 = "Tsubasa"
    n5 = "Akira"
    n6 = "Haku"
    n7 = "Ace"

class lnames:
    n0 = "Amari"
    n1 = "Abiko"
    n2 = "Hori"
    n3 = "Chisaka"
    n4 = "Kato"
    n5 = "Genji"
    n6 = "Chiba"
    n7 = "Ejiri"
    n8 = "Alex"
    n9 = "Fumi"
    na = "Katayama"
    nb = "Tsuda"
    nc = "Yagi"
    nd = "Aguni"
    ne = "Uchida"
    nf = "Nagata"

class colors:
    c0 = "Red"
    c1 = "Magenta"
    c2 = "Lime Green"
    c3 = "Sky Blue"
    c4 = "Black"
    c5 = "Silver"
    c6 = "Pink"
    c7 = "Yellow"
    c8 = "Pico Red"
    c9 = "Pastel Blue"
    ca = "Pastel Green"
    cb = "Gray/Grey"
    cc = "Gold"
    cd = "Tic Blue"
    ce = "Rainbow"
    cf = "Paste Pink"

class fsexuality:
    s1 = "straight"
    s2 = "lesbian"
    s3 = "bisexual"
    s4 = "pansexual"
    
class bsexuality:
    s1 = "straight"
    s2 = "gay"
    s3 = "bisexual"
    s4 = "pansexual"

def commands(command):
    if command == "":
        print("""
Hey, and welcome to cringe creator version 1.0
------------------------------------------
Use commands() for a list of commands!
Use rancreate() to create a random cringe.
More coming soon, probably.
""")


def rancreate():
    
    def line():
        print("----------------------------------")
    class randomchar:
        gender = random.choice(range(3))
        
        if gender == 0:
            fname = random.choice(range(8))
        elif gender == 1:
            fname = random.choice(range(8))
        elif gender == 2:
            fname = random.choice(range(16))
        else:
            raise Exception("Something has gone wrong, contact me on discord.")
        
        lname = random.choice(range(16))
        favcolor = random.choice(range(16))
        
        if gender == 0:
            sxalty = random.choice(range(4))
        elif gender == 1:
            sxalty = random.choice(range(4))
        elif gender == 2:
            sxalty = random.choice(range(8))
        else:
            raise Exception("Something has gone wrong, contact me on discord.")
        
        age = 15 + random.choice(range(20))
        
        if fname == 0:
            rfname = fgnames.n0
        elif fname == 1:
            rfname = fgnames.n1
        elif fname == 2:
            rfname = fgnames.n2
        elif fname == 3:
            rfname = fgnames.n3
        elif fname == 4:
            rfname = fgnames.n4
        elif fname == 5:
            rfname = fgnames.n5
        elif fname == 6:
            rfname = fgnames.n6
        elif fname == 7:
            rfname = fgnames.n7
        elif fname == 8:
            rfname = fbnames.n0
        elif fname == 9:
            rfname = fbnames.n1
        elif fname == 10:
            rfname = fbnames.n2
        elif fname == 11:
            rfname = fbnames.n3
        elif fname == 12:
            rfname = fbnames.n4
        elif fname == 13:
            rfname = fbnames.n5
        elif fname == 14:
            rfname = fbnames.n6
        elif fname == 15:
            rfname = fbnames.n7
            
        if lname == 0:
            rlname = lnames.n0
        elif lname == 1:
            rlname = lnames.n1
        elif lname == 2:
            rlname = lnames.n2
        elif lname == 3:
            rlname = lnames.n3
        elif lname == 4:
            rlname = lnames.n4
        elif lname == 5:
            rlname = lnames.n5
        elif lname == 6:
            rlname = lnames.n6
        elif lname == 7:
            rlname = lnames.n7
        elif lname == 8:
            rlname = lnames.n8
        elif lname == 9:
            rlname = lnames.n9
        elif lname == 10:
            rlname = lnames.na
        elif lname == 11:
            rlname = lnames.nb
        elif lname == 12:
            rlname = lnames.nc
        elif lname == 13:
            rlname = lnames.nd
        elif lname == 14:
            rlname = lnames.ne
        elif lname == 15:
            rlname = lnames.nf
        
        if favcolor == 0:
            color = colors.c0
        elif favcolor == 1:
            color = colors.c1
        elif favcolor == 2:
            color = colors.c2
        elif favcolor == 3:
            color = colors.c3
        elif favcolor == 4:
            color = colors.c4
        elif favcolor == 5:
            color = colors.c5
        elif favcolor == 6:
            color = colors.c6
        elif favcolor == 7:
            color = colors.c7
        elif favcolor == 8:
            color = colors.c8
        elif favcolor == 9:
            color = colors.c9
        elif favcolor == 10:
            color = colors.ca
        elif favcolor == 11:
            color = colors.cb
        elif favcolor == 12:
            color = colors.cc
        elif favcolor == 13:
            color = colors.cd
        elif favcolor == 14:
            color = colors.ce
        elif favcolor == 15:
            color = colors.cf
            
        if sxalty == 0:
            sexu = fsexuality.s1
        elif sxalty == 1:
            sexu = fsexuality.s2
        elif sxalty == 2:
            sexu = fsexuality.s3
        elif sxalty == 3:
            sexu = fsexuality.s4
        elif sxalty == 4:
            sexu = bsexuality.s1
        elif sxalty == 5:
            sexu = bsexuality.s2
        elif sxalty == 6:
            sexu = bsexuality.s3
        elif sxalty == 7:
            sexu = bsexuality.s4
            
        if gender == 0:
            gen = "a girl "
        elif gender == 1:
            gen = "a boy "
        else:
            gen = "non-binary "
            
        line()
        print("Your character is " + rfname + " " + rlname )
        print("They are " + gen + "and are " + sexu)
        print("Their favorite color is " + color)
        line()
        
commands()