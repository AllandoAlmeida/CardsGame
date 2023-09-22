from top_geek import deck


def play_turn(
    p1_deck: list[dict],
    p2_deck: list[dict],
    main_deck: list[dict]
) -> None:
    p1_card = deck.draw_card(p1_deck)
    p2_card = deck.draw_card(p2_deck)
    attr_to_compare = deck.get_random_attr(p1_card)
    if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
        deck.put_cards_to_base(p1_deck, p1_card, p2_card, *main_deck)
        print(f"{p1_card['name']} DEFEAT {p2_card['name']}")
    elif p1_card[attr_to_compare] < p2_card[attr_to_compare]:
        deck.put_cards_to_base(p2_deck, p1_card, p2_card,  *main_deck)
        print(f"{p2_card['name']} DEFEAT {p1_card['name']}")
    else:
        main_deck.extend([p1_card, p2_card])
        print("DRAW")


def play_game() -> None:
    geek_deck = deck.generate_deck()
    p1_deck, p2_deck = deck.split_deck(geek_deck)
    mount_deck = []
    while True:
        play_turn(p1_deck, p2_deck, mount_deck)
        if len(p1_deck) == 0:
            return print("PLAYER 2 WINS")
        if len(p2_deck) == 0:
            return print("PLAYER 1 WINS")
