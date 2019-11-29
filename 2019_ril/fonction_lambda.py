from random import randint


# Fonction simple
def square(x):
    return x ** 2


# Fonction Lambda
square = lambda x: x ** 2

tab = [randint(0, 500) for x in range(10)]
# Map applique une fonction (ici la fonction lambda square) sur tous les éléments d'un tableau
tab_power_2 = list(map(square, tab))
print("Tab = " + str(tab))
print("Tab_power_2 = " + str(tab_power_2))
