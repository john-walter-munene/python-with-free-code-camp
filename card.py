class Card:
    """Creating my cards class"""
    def __init__(self, suit, rank):
        """Initializing card attributes"""
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        """Generate the print statement for our card"""
        return f"{self.rank['rank']}  of {self.suit}"
        
    