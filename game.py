import random

def roll():
    umum = 100
    langka = 18
    epic = 5
    roll = random.randint(1,100)
    if roll <= epic:
        return 'Jir cit ya'
    elif roll <= langka and roll >= epic:
        return 'Mayan ga siehh.. dapet langka'
    else:
        return 'Yahh dapet umum'
    
def main():
    rolling = roll()
    rolling
    print(rolling)
main()