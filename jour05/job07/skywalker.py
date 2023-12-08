import math

notes =  list(range(101))
l=(15, 24, 49, 72, 83)


def note (l): 
    for i in range (len(l)):
        if l[i] > 40 :
            print (f"Pour une note de {l[i]}, le test est reussi")

        else:
            print (f"Pour une note de {l[i]} le test est un echec")
note(l)


def arrondi (note_initiale):
    return math.ceil(((note_initiale) - 3) / 5) * 5

note_initiale = len(l)

l_note_arrondie = [arrondi(note) for note in l]

print(f"Note initiale : {l}")
print(f"Note arrondie : {l_note_arrondie}")



