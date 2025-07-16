import argparse
import random
from thefuzz import process
import copy



class blackjack:

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.chip_count = []

        self.player_hand_score = 0
        self.dealer_hand_score = 0

        self.card_rank_dict = {
            'A': 11,
            'K': 10,
            'Q': 10,
            'J': 10,
            'T': 10,
        }

        self.handsize = 2

        self.deck = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠']

    def game_state(self):
        game = blackjack()
        # print(len(self.deck))
        print('\n')
        print('Dealers Hand:\n')
        game.deal_hand('dealer', 2, deck=game.deck)
        dealer_hand_shown = copy.copy(game.dealer_hand)
        dealer_hand_shown[1] = "??"
        print(dealer_hand_shown)

        print('\n')
        
        print('Your Hand:\n')
        game.deal_hand('player', 2, deck=game.deck)
        print(game.player_hand)

        hit = input("Hit? (y/n) ")

        if hit == "y":
            print('hit')
            game.deal_hand('player', 1, deck=game.deck)
            # print(game.player_hand)

        game.score_hand('player', game.player_hand)
        game.score_hand('dealer', game.dealer_hand)

        game.dealer_logic(dealer_score = game.dealer_hand_score, player_score =game.player_hand_score, deck=game.deck)

        # game.dealer_hand_score = 0
        # game.score_hand('dealer', game.dealer_hand)


        # \033 is the escape character (ASCII code 27 in octal).
        # [2J clears the entire screen.
        # [H moves the cursor to the top-left corner.
        print("\033[2J\033[H")

        print('\n')
        print('Dealers Hand:\n')
        print(game.dealer_hand)
        print(game.dealer_hand_score)
        print('\n')
        
        print('Your Hand:\n')
        print(game.player_hand)
        print(game.player_hand_score)

        # print(game.player_hand_score)
        # print(game.dealer_hand_score)

        if game.dealer_hand_score > 21 and game.player_hand_score <=21:
            print('Dealer Busts!')
            print('Player wins!')
        elif game.dealer_hand_score <= 21 and game.player_hand_score > 21:
            print('Player Busts!')
            print('Dealer wins!')
        elif game.dealer_hand_score > 21 and game.player_hand_score > 21:
            print('Double Bust!')
            print('Draw!')
        elif game.dealer_hand_score > game.player_hand_score:
            print('Dealer wins!')
        elif game.dealer_hand_score < game.player_hand_score:
            print('Player wins!')
        elif game.dealer_hand_score == game.player_hand_score:
            print('Draw!')

        
    
    def deal_hand(self, actor, numcards, deck):
        for card in range(numcards):
            # rand_temp = random.randint(0,len(self.deck))
            # try:
            # card_temp = self.deck.pop(rand_temp)
            # except:
                # rand_temp = random.randint(0,len(self.deck))
                # card_temp = self.deck.pop(rand_temp)
            card_temp = random.choice(self.deck)
            index_temp = self.deck.index(card_temp)
            if index_temp in range(len(self.deck)):
                # print(self.deck)
                # print(len(self.deck))
                # print(range(len(self.deck)))
                # print(index_temp)
                # print(card_temp)
                self.deck.remove(card_temp)
                # print(len(self.deck))
            else:
                print(card_temp)
                print(self.deck.index(card_temp))
            # self.deck = self.deck - card_temp
            # self.deck = list(self.deck)
            # self.deck.remove(card_temp)

            if actor == 'player':
                self.player_hand.append(card_temp)
            elif actor == 'dealer':
                self.dealer_hand.append(card_temp)
        # print(self.player_hand)
        # return self

    def score_hand(self, actor, hand):
        score = 0
        ace_in_hand = False
        for card in range(len(hand)):
            # print(card)
            rank = hand[card][0]
            if rank == "A":
                ace_in_hand = True
            # print(rank)

            if rank in self.card_rank_dict.keys():
                rank_value = self.card_rank_dict[rank]
                score = score + rank_value
            else:
                score = score + int(rank)
            # print(score)
        if score > 21 and ace_in_hand:
            score = score - 10

        if actor == 'player':
            self.player_hand_score =  self.player_hand_score + score
        elif actor == 'dealer':
            self.dealer_hand_score =  self.dealer_hand_score + score

    def dealer_logic(self, dealer_score, player_score, deck):
        

        if dealer_score == 15:
            self.deal_hand('dealer', 1, deck=self.deck)
            self.dealer_hand_score = 0
            self.score_hand('dealer', self.dealer_hand)

        if dealer_score < player_score and dealer_score < 21:
            self.deal_hand('dealer', 1, deck=self.deck)
            self.dealer_hand_score = 0
            self.score_hand('dealer', self.dealer_hand)

        # finite = 3
        # i = 0
        # while dealer_score < 21 or dealer_score < player_score or i < finite:
        #     self.dealer_hand_score = 0
        #     self.deal_hand('dealer', 1, deck=self.deck)
        #     self.score_hand('dealer', self.dealer_hand)
        #     i += 1

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
        blackjack().game_state()
    elif mode == 'poker':
        print("Under construction")

    else:
        print(mode)
        print(args)

