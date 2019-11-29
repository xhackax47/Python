# Fontion qui supprime les voyelles d'une chaîne String
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return "/".join([char for char in string
                     if char.lower() not in vowels])


# Fontion qui détermine si l'objet est un isogramme (Chaque lettre se répète autant de fois)
def is_isogram(string):
    dictionnary = {char: string.count(char) for char in string}
    unique_values = set(dictionnary.values())
    return len(unique_values) == 1


print("Suppression voyelles de samy : " + str(remove_vowels("samy")))
print("Suppression voyelles de SAMY : " + str(remove_vowels("SAMY")))
print("Savoir si c'est un isogramme : " + str(is_isogram("program")))
print("Savoir si c'est un isogramme : " + str(is_isogram("aabbccdd")))
