import random

DINO_NAMES = (
    "Mandissaurus Rex",
    "Janeodonte",
    "Emmanu Raptor",
    "Kizzrátops",
    "Rosezilla",
    "Abelrodáctilo"
)


def generate_dino_deck() -> list[dict]:
    dino_cards = []

    for dino_name in DINO_NAMES:
        dino_dict = {
            "name": dino_name,
            "strength": 2,
            "agility": 4,
            "height": 1
        }

        dino_cards.append(dino_dict)

    return [
        {
            "name": dino_name,
            "strength": random.randint(1, 10),
            "agility": round(random.uniform(0, 10), 1),
            "height":  round(random.uniform(0, 10), 2)
        }
        for dino_name in DINO_NAMES
    ]


def split_deck(deck: list[dict]) -> tuple[list[dict], list[dict]]:
    half_deck = len(deck) // 2

    random.shuffle(deck)

    return (deck[:half_deck], deck[half_deck:])


def get_random_attr(card: dict) -> str:
    card_keys = [key for key in card.keys() if key != "name"]

    return random.choice(card_keys)