from random import shuffle
import json

def deck_load():
    with open('deck.json', 'r') as file:
        deck = json.load(file)
        deck1, deck2, deck3, deck4 = [deck["1"], deck["2"],
                                      deck["3"], deck["4"]]
        deck = deck1 + deck2 + deck3 + deck4

    return deck, deck1, deck2, deck3, deck4


def game_preparation(deck):
    shuffle(deck)
    del deck[:2]  # tossing certain number of cards (here: 2 toss)

    return deck


def card_distribution(deck):
    # change to loop in which each player is a item
    player_hand = []
    casino_hand = []
    player_hand.append(deck[0])
    deck.pop(0)
    casino_hand.append(deck[0])
    deck.pop(0)

    return player_hand, casino_hand


def player_draw(player_hand):
    player_hand.append(deck[0])
    deck.pop(0)

    # warunek jeżeli ręka ma więcej niż 21 pkt


def casino_draw(casino_hand):
    while len(casino_hand) < 3:  # warunek testowy (po implementacji pkt zmienić)
        casino_hand.append(deck[0])
        deck.pop(0)


deck, deck1, deck2, deck3, deck4 = deck_load()
deck = game_preparation(deck)
player_hand, casino_hand = card_distribution(deck)
print('This version of PyJack doesn\'t support the hand split!')
while True:
    print(f'Casino: {casino_hand}\n'
          f'Player: {player_hand}')
    decision = input('--- [h]it, [s]tay ---\n'
                     'Decision?: ')
    if decision == 'h' or decision == 'hit':
        print('* You made a hit. *')
        player_draw(player_hand)
    elif decision == 's' or decision == 'stay':
        print('* You stayed. *')
        casino_draw(casino_hand)
        print(f'Casino: {casino_hand}\n'
              f'Player: {player_hand}')
        break
    else:
        print('Provided decision doesn\'t exist. Try again!')
        continue
