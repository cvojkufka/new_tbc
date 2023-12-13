"""
Christopher Vojkufka
christopher.vojkufka@bsu.edu

My Final Project
Thank you Professor Harris!

"""
"""
import my new tbc library
create a character for player1
if the stats look okay, continue to create a monster at random and assign the fight
if the state are not okay, make the player choose a different class until conclusion
fight will commence until one player dies
at the end ask if they want to play again
if not, close
if yes, redo everything above end statement until they do want to quit. 
check for any sneaky inputs.
"""

import new_tbc


def main():
    
    print("Welcome to Turn Based Combat Plus!")
    
    playAgain = True
    
    while playAgain:
        hero = new_tbc.Character()
        player1 = hero.createCharacter()
        player1.printStats()
        
        confirm = input("Is this selection okay? ")
        print("")
    
        keepGoing = True
        
        while keepGoing:
            
            if confirm.lower() == "yes":
                player1.printStats()
                keepGoing = False
            elif confirm.lower() == "no":
                player1 = hero.createCharacter()
                player1.printStats()
                print("")
                confirm = input("Is this selection okay? ")
            else:
                print("")
                print("Not a choice. Please try again")
                print("")
                confirm = input("Is this selection okay? ")
                print("")
        
        monster = new_tbc.Character()
        player2 = monster.createMonster()
        player2.printStats()
        
        new_tbc.fight(player1, player2)
        game = True
        
        while game:
            play = input("Do you want to play again? (y/n) ")
            print("")
            play.lower()
            if play == "y":
                playAgain = True
                game = False
            elif play == "yes":
                playAgain = True
                game = False
            elif play == "n":
                playAgain = False
                game = False
            elif play == "no":
                playAgain = False
                game = False
            else:
                print("Please enter 'y' or 'n': ")
    
if __name__ == "__main__":
    main()

