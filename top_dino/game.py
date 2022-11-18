from . import deck

def play():
    dino_deck = deck.generate_dino_deck()

    p1_deck, p2_deck = deck.split_deck(dino_deck)

    # TODO:
    # - Retirar printagem do escopo do play e realocar para outro módulo
    # - battle_printing -> 

    for index, p1_card in enumerate(p1_deck):
        print()
        attr_to_compare = deck.get_random_attr(p1_card)
        p2_card = p2_deck[index]

        print("p1_card -> ", p1_card)
        print("p2_card -> ", p2_deck[index])
        print("attr_to_compare -> ", deck.get_random_attr(p1_card))

        if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
            print(f"{p1_card['name']} WINS!")
        elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
            print(f"{p2_card['name']} WINS!")
        else:
            print("DRAW!")