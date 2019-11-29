pizzas = {"Anchois": 9.60,
          "Jambon": 10.5,
          "Royale": 12}

name = input("Entrer le nom d'une pizza \n")
total = 0

# Premiere méthode
if name in pizzas:
    print(f"Prix Première Pizza : {pizzas[name]}")
else:
    print("Pizza inconnue")

# Deuxième méthode
name = input("Entrer le nom d'une pizza \n")
try:
    print(f"Prix Deuxième Pizza : {pizzas[name]}")
except KeyError:
    print("Pizza inconnue")

# Troisième méthode
name = input("Entrer le nom de la troisième pizza \n")
if price := pizzas.get(name) is not None:
    print(f"Prix Troisième Pizza : {pizzas[name]}")
else:
    print("Pizza inconnue")
