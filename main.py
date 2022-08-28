# This is the code where the game is run
from card import Card
from deck import Deck
from hand import Hand        
class Game:
    """The class that runs the game"""
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            # Let user input the number of games they would wish to play
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number: ")
                
        while game_number <= games_to_play:
            game_number += 1
            
            # Create a dec and shuffle it
            deck = Deck
            deck.shuffle
            
            #Create a players, hand and setting it to hands object
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            
            # Loop to add a card to the player and the dealer from the deck
            for i in range(2):
                player_hand.add_card(deck.deal(2))
                dealer_hand.add_card(deck.deal(1))
                
            print()
            # Adding a divider
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice is not ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()
                     
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()
                
            dealer_hand.display(show_all_dealer_cards=True)
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print("Final Results")
            print("You hand: ", player_hand_value)
            print("Dealers hand: ", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, True)
        print("\nThanks for playing! Come play again")
            
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """Verify winner"""
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! :-(")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! :-)")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have a blackjack! Tie! :-|")
                return True
            elif player_hand.is_blackjack():
                print("You have a blackjack. You win! :-)")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack. Dealer wins :-(")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie :-|")
            else:
                print("Dealer wins :-(")
        return False
        
g = Game()
g.play()
    