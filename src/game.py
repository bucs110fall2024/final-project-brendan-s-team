from src.button import Button

class Game():
    def __init__(self, screen, playerhand, dealerhand):
        """
        uses logic to calculate the winner of the game
        args: playerhand - players hand size
        dealerhand - dealers hand size
        return
        """
        self.playerhand = playerhand
        self.dealerhand = dealerhand

        def game_logic(self):
            if self.playerhand == 21:
                blackjack = Button((0,0), (500,300), self.screen, 'BlackJack!', (110,110,110))
                blackjack.draw()
                # pcards.clear()
                # playerhand = 0
                # hand_x = 375
            elif self.playerhand > 21:
                pbust = Button((0,0), (500,300), self.screen, 'Bust! You Lose', (110,110,110))
                pbust.draw()
