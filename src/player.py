#from card import Card

class Player():
    def __init__(self, hand_size = 0):
        """
        initializes the player
        args: hand_size - size of the players hand
        """
        self.hand_size = hand_size
    
    def hit(self, hand_size):
        """
        allows the player to 'hit' (draw another card)
        args:
        return: hand_size
        """
        self.hand_size = hand_size
        if self.hand_size > 21:
            pass
    
    def stand(self, hand_size):
        """
        allows the player to 'stand', then determines the winner of the game
        args: hand_size - the size of the players hand
        return: win (boolean)
        """