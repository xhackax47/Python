from random import randint

# Jeu du Plus ou Moins en Python

# Declaration variables

to_guess = randint(0, 100)
is_notfound = True

# Tant que variable is_notfound = True
while is_notfound:

    # On demande un nombre à l'utilisateur
    number = input('Entrer un nombre \n')

    # Si le contenu de number est un digit on cast en int la variable number
    if number.isdigit():
        number = int(number)

        # Si le number est égal au numéro à trouver
        if number == to_guess:
            print("Numéro trouvé !!! C'était bien le " + str(number))
            is_notfound = False
            break

        # Sinon si le number est plus grand que le numéro à trouver
        elif number > to_guess:
            print("Numéro trop haut ! \n")

        # Sinon si le number est plus petit que le numéro à trouver
        elif number < to_guess:
            print("Numéro trop bas ! \n")
    else:

        # Message erreur si on entre pas un int dans number
        print("Mauvais caractère (Nombre attendu) \n")
