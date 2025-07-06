import argparse
import random
from thefuzz import process



class blackjack:

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.chip_count = []

        self.handsize = 2

        self.deck = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠']

    def deal_hand(self):
        # for card in range(self.handsize):
            
            # self.player_hand.append(random.random())
        self.player_hand = self.player_hand + random.sample(self.deck, k=2)

        print(self.player_hand)


# blackjack().deal_hand()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select blackjack")


    parser.add_argument("-g", '--game', type=str, help="Game mode select")

    gamemodes = ['blackjack', 'poker']

    mode = None


    args = parser.parse_args()

    if args.game in gamemodes:
        mode = args.game
    else:
        fuzzfind = process.extract(args.game, choices= gamemodes, limit=1)
        game_maybe = fuzzfind[0][0]
        score_maybe = fuzzfind[0][1]
        if score_maybe > 84:
            print(f'Did you mean {game_maybe}?')
        else:
            print(f'Game options are {gamemodes}')


    if mode == 'blackjack':
        blackjack().deal_hand()
    elif mode == 'poker':
        print("Under construction")

    else:
        print(mode)
        print(args)

