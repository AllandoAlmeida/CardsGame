from .students import student_names
import random


def generate_deck() -> list[dict]:
    geek_deck = []
    for student_name in student_names:
        geek_card = {
            "name": student_name,
            "books_read": random.randint(1, 1000),
            "series_watched": random.randint(1, 1000),
            "movies_watched": random.randint(1, 1000),
        }
        geek_card["overall"] = (
            geek_card["books_read"]
            + geek_card["movies_watched"]
            + geek_card["series_watched"]
        ) / 3
        geek_deck.append(geek_card)  # Adicione o geek_card ao geek_deck

    return geek_deck


def split_deck(deck: list[dict]) -> tuple[list[dict], list[dict]]:
    random.shuffle(deck)
    half_index = len(deck) // 2
    if len(deck) % 2 != 0:
        deck = deck[:-1]
    p1_deck = deck[:half_index]
    p2_deck = deck[half_index:]

    return p1_deck, p2_deck  # Retorna as duas listas, não seus comprimentos


def get_random_attr(card: dict) -> str:
    card_keys = [key for key in card.keys() if key != "name"]
    return random.choice(card_keys)


def draw_card(deck: list[dict]) -> dict:
    return deck.pop()


def put_cards_to_base(deck: list[dict], *cards) -> None:
    deck[:] = list(cards) + deck
