class Person:

    def __init__(self, first_name, last_name, *args, **kwargs):
        """
        Constructeur de la classe et declaration des attributs de la classe avec typage
        :param first_name: string
        :param last_name: string
        :param part:
        :return : string
        """
        print("Construction de l'objet")
        self.first_name = first_name
        self.last_name = last_name

    def __del__(self):
        """
        Destructeur de la classe
        :return:
        """
        print("Destruction de l'objet")

    def __enter__(self):
        """
        Entrée du with (Allouer/Ouvrir ce que l'on veut)
        :return: self
        """
        print("Enter !")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Sortie du with (Nettoyer allocation/ouverture)
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print("Exit !")

    def print(self):
        """
        Affiche une fstring avec le first_name et le last_name
        :return: 
        """
        print(f'FirstName : {self.first_name} & LastName : {self.last_name}')


with Person("Test FirstName With", "Test LastName With") as person:
    person.print()

# Déclaration variables

first_name = "Test FirstName"
last_name = "Test LastName"

tab_person2 = ["Test FirstName 2", "Test LastName 2"]

dictionnary_person3 = {'first_name': "Test FirstName 3", 'last_name': "Test LastName 3"}

# Instanciation des objets person & person2

person = Person(first_name, last_name)
person2 = Person(*tab_person2)
person3 = Person(**dictionnary_person3)

# Affichage des objets

print("Personne 1 = First name : " + person.first_name + " Last name : " + person.last_name)
print("Personne 2 = First name : " + person2.first_name + " Last name : " + person2.last_name)
print("Personne 3 = First name : " + person3.first_name + " Last name : " + person3.last_name)
