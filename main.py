import random


def generate_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    for suit in suits:
        for i in range(13):
            num = i + 1
            if num == 1:
                name = 'Ace'
                value = 11
            elif num == 11:
                name = 'Jack'
                value = 10
            elif num == 12:
                name = 'Queen'
                value = 10
            elif num == 13:
                name = 'King'
                value = 10
            else:
                name = str(num)
                value = num
            key = f'{name} of {suit}'
            deck = deck + [(key, value)]
    return deck


def get_card(input_deck):
    num_items = len(input_deck)
    index = random.randint(0, num_items - 1)
    card = input_deck[index]
    del input_deck[index]
    return card


def deal_cards(input_deck, cards_to_deal):
    score = 0
    for i in range(cards_to_deal):
        card = get_card(input_deck)
        score += card[1]
    return score


def main():
    deck = generate_deck()
    dealer_score = deal_cards(deck, 2)
    player_score = deal_cards(deck, 2)
    print(f'Dealer has {dealer_score}')
    print(f'Player has {player_score}, stick (s) or twist (t)?')
    while True:
        response = input()
        if response == 't':
            player_score += deal_cards(deck, 1)
            if player_score == 21:
                print('Blackjack')
                break
            if player_score > 21:
                print(f'Bust - you got {player_score}')
                break
            else:
                print(f'Player has {player_score}, stick (s) or twist (t)?')
        if response == 's':
            break


main()
