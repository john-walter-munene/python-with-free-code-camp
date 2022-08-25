class Hand:
    
    """A hand to keep track of the cards"""
    def __init__(self, dealer=False):
        """"Initializing hand attributes"""
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        """Take a card from the list"""
        self.cards.extend(card_list)
        
    def calculate_value(self):
        """Calculate the value of a hand"""
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        """Return value calculated"""
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        """Return a black jack if value is 21"""
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False):
        """Display info about your hand"""
        print(f'''{"Dealer's " if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        
        if not self.dealer:
            print("value ", self.get_value())
        print()