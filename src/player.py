import Card

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
    
    def stand(self):
        """
        allows the player to 'stand', then determines the winner of the game
        args:
        return: win (boolean)
        """