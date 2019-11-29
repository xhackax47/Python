from random import shuffle

# Jeu de cartes sous Python

# Declaration variables

cards = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R')
cards_symbols= ('♣', '♥', '♠', '♦')

# Expression de boucle For de compréhension de liste pour ajout dans le deck des cartes

cards_deck = [card + card_symbol for card in cards for card_symbol in cards_symbols]

# Mélange des cartes du deck

shuffle(cards_deck)

# Affichage des résultats

print("Contenu du deck : " + str(cards_deck))
print("Nombre de cartes présentes dans le deck : " + str(len(cards_deck)))

# Expression FOR classique

"""
for card in cards:
    for card_symbol in cards_symbols:
        cards_deck.append(card+card_symbol)

print(cards_deck)
print(len(cards_deck))
"""