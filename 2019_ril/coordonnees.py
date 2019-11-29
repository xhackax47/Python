# Déclarations variables

Aix = (1.5, 6.8)
a, *b = "10123"
unicode = u"Test Unicode"
non_interprete = r"C:\Windows\Users\Nabil"
retraitStartEnd = "Test retrait du début vers la fin"
retraitEndStart = "Test retrait du début vers la fin"
first_name= "firstName"
last_name= "lastName"


def get_coord(town):
    return town


lat, lng = get_coord(Aix)

print("Latitude : " + str(lat) + "°")
print("Longitude : " + str(lng) + "°")
print("A, récupère le premier caractère, B récupère tout le reste = " + a, b)
print("Version unicode" + unicode)
print("Variable non interprété (\ n) : " + non_interprete)
print("Récupération des 2 derniers caractères de la chaîne : " + retraitStartEnd[-2:])
print("Retrait des 2 derniers caractères de la chaîne : " + retraitStartEnd[:-2])

#Concatenation String

print("Concatenation %s : " + "FULL NAME IS %s %s" % (first_name, last_name))
print("Concatenation {} : " + "FULL NAME IS {0} {1}".format(first_name, last_name))
print("Concatenation %s : " + "FULL NAME IS {nom} {prenom}".format(nom = first_name, prenom= last_name))
print(f"Concatenation fstring : FULL NAME IS  {first_name}, {last_name}")
