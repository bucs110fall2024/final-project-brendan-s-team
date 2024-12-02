
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  Fall, 2024

## Team Members

Brendan Kearney

***

## Project Description

A simple blackjack game with antes, and all the typical features of blackjack

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Hit
2. Stand
3. << Feature 3 >>
4. << Feature 4 >>
5. << Feature 5 >>

### Classes

- Card
    - contains all of the data a card needs, such as a suit, rank, and value (used to calculated the value of a hand)


## ATP

Step 1: Start Game
    - Open terminal, navigate to project folder, type: python main.py
    - Press enter
    - **expected outcome**
    - green screen with a Start Game button appears

Step 2: Play Game
    - click on the 'Play Game' button in the center of the screen
    - **expected outcome**
    - game should switch to a UI with hit, stand, ante options, and draw the first 3 cards

Step 3: Ante
    - click on either the +50 or -50 buttons to     raise or lower your ante
    **expected outcome**
    - bar representing your ante should increase or decrease depending on the selected amount you chose to ante

Step 4: Hit
    - click on the button to 'hit'
    - **expected outcome**
    - a card should appear in your hand, and it should be added to your total hand value
    - if it is > 21, you bust
    - under 21, you can either hit again or stand
    - = 21, blackjack!

Step 5: Stand
    - click on the button to 'stand'
    - **expected outcome**
    - dealer should draw cards depending on if their hand is below or above 17
    - game should calculate the winner and display it properly
