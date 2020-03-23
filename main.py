from random import shuffle


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
    shuffle(deck)
    return deck


def deal_card(input_deck):
    card = input_deck[0]
    del input_deck[0]
    return card


def evaluate_score(input_lst):
    score = 0
    for card, value in input_lst:
        score += value
    return score


def blackjack_bust_check(input_score):
    if input_score == 21:
        result = 'Blackjack!'
    elif input_score > 21:
        result = 'Bust!'
    else:
        result = False
    return result


players = ['Dealer', 'Ali']


def main():
    dealer_hand = []
    player_hand = []
    deck = generate_deck()
    for i in range(2):
        for player in players:
            card = deal_card(deck)
            if player == 'Dealer':
                dealer_hand.append(card)
            else:
                player_hand.append(card)
    print(f'Dealer\'s first card is {dealer_hand[0][0]}')
    print(f'Dealers current score is {dealer_hand[0][1]}')
    player_score = evaluate_score(player_hand)
    while True:
        print(f'Your score is {player_score}')
        print('Stick (s) or twist (t)?')
        response = input()
        if response == 's':
            player_blackjack_bust = blackjack_bust_check(player_score)
            break
        elif response == 't':
            card = deal_card(deck)
            player_hand.append(card)
            player_score = evaluate_score(player_hand)
            player_blackjack_bust = blackjack_bust_check(player_score)
            if player_blackjack_bust:
                break

    dealer_score = evaluate_score(dealer_hand)
    while True:
        if dealer_score < 17:
            card = deal_card(deck)
            dealer_hand.append(card)
            dealer_score = evaluate_score(dealer_hand)
        else:
            break
    dealer_blackjack_bust = blackjack_bust_check(dealer_score)

    if player_blackjack_bust:
        print(f'Player Result: {player_blackjack_bust}... Score {player_score}')
    else:
        print(f'Player Score = {player_score}')

main()
