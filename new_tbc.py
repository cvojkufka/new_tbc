# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:07:27 2023

Christopher Vojkufka
christopher.vojkufka_tbc.py
"""
"""
import random into the class
create the character class that takes in the object
initialize variables given by instructor
set the properties and appropriate setters to accompany them so bugs are harder to happen
"""
import random

class Character(object):
    
    def __init__(self, name = "Hero", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 2, maxHitPoints = 10):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        self.maxHitPoints = maxHitPoints
        
    @property
    def name(self):
        return self.__name
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @property
    def armor(self):
        return self.__armor
    
    @property
    def maxHitPoints(self):
        return self.__maxHitPoints
    """
    """
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            newValue = value
        else:
            print("only strings allowed. Setting to Hero")
            newValue = "Hero"
        
        self.__name = newValue
        
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            if value >= 0:
                newValue = value
            else:
                print("only positive values or zero. Setting to ten")
                newValue = 10
        else:
            print("only integers allowed. Setting to ten")
            newValue = 10
        
        self.__hitPoints = newValue
    
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                newValue = value
            elif value > 100:
                print("only chance bewteen 1 and 100. Setting to fifty")
                newValue = 50
            else:
                print("only positive values or zero. Setting to fifty")
                newValue = 50
        else:
            print("only integers allowed. Setting to fifty")
            newValue = 50
        
        self.__hitChance = newValue
        
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                newValue = value
            else:
                print("only positive values or zero. Setting to five")
                newValue = 5
        else:
            print("only integers allowed. Setting to five")
            newValue = 5
        
        self.__maxDamage = newValue
        
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                newValue = value
            else:
                print("only positive values or zero. Setting to two")
                newValue = 2
        else:
            print("only integers allowed. Setting to two")
            newValue = 2
        
        self.__armor = newValue
        
    @maxHitPoints.setter
    def maxHitPoints(self, value):
        if type(value) == int:
            if value >= 0:
                newValue = value
            else:
                print("only positive values or zero. Setting to ten")
                newValue = 10
        else:
            print("only integers allowed. Setting to ten")
            newValue = 10
        
        self.__maxHitPoints = newValue
        
    """
    create a character for player1
    print the options for player1
    classchoice will get the number they choose
    assign information appropriately
    if not a choice, print try again
    return a character that suffices criteria
    """
     
    def createCharacter(self):

        keepGoing = True
        
        while keepGoing:
            print("Select a class:")
            print("1) Warrior")
            print("2) Mage")
            print("3) Rogue")
            print("4) Tank")
            
            print("")
            classChoice = input("Enter the number of your choice: ")
            print("")
            
            if classChoice == "1":

                character = Character(name = "Warrior", hitPoints = 15, hitChance = 60, maxDamage = 8, armor = 5, maxHitPoints = 15)
                keepGoing = False
                
            elif classChoice == "2":

                character = Character(name = "Mage", hitPoints = 8, hitChance = 70, maxDamage = 10, armor = 2, maxHitPoints = 8)
                keepGoing = False
                
            elif classChoice == "3":

                character = Character(name = "Rogue", hitPoints = 12, hitChance = 80, maxDamage = 6, armor = 3, maxHitPoints = 12)
                keepGoing = False
                
            elif classChoice == "4":
                
                character = Character(name = "Tank", hitPoints = 25, hitChance = 30, maxDamage = 15, armor = 8, maxHitPoints = 25)
                keepGoing = False
                
            else:
                print("You chose a class that doesn't exist. Please try again.")
                print("")
            
        return character
    """
    create monster with player 2
    get a random number between 1 and 4
    assign character to play 2 approriately
    return the character information
    """
        
    def createMonster(self):
        
        num = random.randint(1,4)
        
        if num == 1:
            
            character = Character(name = "Orc", hitPoints = 12, hitChance = 60, maxDamage = 8, armor = 5, maxHitPoints = 12)
            
        elif num == 2:
            
            character = Character(name = "Tyrant", hitPoints = 15, hitChance = 65, maxDamage = 9, armor = 5, maxHitPoints = 15)
            
        elif num == 3:
            
            character = Character(name = "Goblin", hitPoints = 8, hitChance = 70, maxDamage = 5, armor = 3, maxHitPoints = 8)
            
        elif num == 4:
            
            character = Character(name = "Dragon", hitPoints = 30, hitChance = 40, maxDamage = 10, armor = 6, maxHitPoints = 30)
            
        return character
    
    """
    make the print stats method which takes self as the parameter
    print the stats of the character the user created 
    """
        
    def printStats(self):
        print(f"{self.__name}\n==================")
        print(f"Hit points: {self.__hitPoints}")
        print(f"Hit chance: {self.__hitChance}")
        print(f"Max damage: {self.__maxDamage}")
        print(f"Armor: {self.__armor}")
        print("")
        
    """
    define the heal function that takes player1
    if your hitpoints are less than your max hitpoints
    your max heal will be the difference between your max and your now hitpoints
    get a random number between 5 and your maxheal
    heal for that amount
    otherwise, print a statement
    """
        
    def heal(self):
        if self.__hitPoints < self.__maxHitPoints:
            maxHeal = self.__maxHitPoints - self.__hitPoints
            healAmount = min(5, maxHeal)
            self.__hitPoints += healAmount
            print(f"{self.__name} healed for {healAmount} HP.")
        else:
            print(f"{self.__name} is already at maximum health.")

        print(f"{self.__name}'s current HP: {self.__hitPoints}")
 
    """
    define the hit method inside character that takes self and enemy as parameters
    get a random chance from 0 to 100
    get a random damage between 1 and maxdamage of self
    if the chance is less than the self hitchance, print strings to indicate that characters are acting
    else, set the damage to 0 and print that self missed
        
    if the enemy armor is greating than or equal to damage, do not remove hitPoints
    else, update hitpoints
    """
        
    def hit(self, enemy):
        chance = random.randint(0, 100)
        damage = random.randint(1, self.__maxDamage)
        
        if chance <= self.__hitChance:
            print(f"{self.__name} hits {enemy.__name}...")
            print(f" for {damage} points of damage!")
            print(f"{enemy.__name}'s armor can asborb {enemy.__armor} points.")
            print("")
        else:
            damage = 0
            print(f"{self.__name} missed!")
            print("")
            
        if enemy.__armor >= damage:
            enemy.__hitPoints = enemy.__hitPoints
        else:
            enemy.__hitPoints = enemy.__hitPoints - damage + enemy.__armor
            
        """
        define the fight attribute that takes in player 1 and player 2
        loop the fight but this time take input to see what the player wants to do
        if hte player wants to heal, check for maxhitpoints and hit appropriately
        if the player wants to fight, continue to the next round
        check for sneaky input
        """
def fight(player1, player2):
    user = input("Press ENTER to begin fight!")
    keepGoing = True
    while keepGoing:
        
        choice = True
        player1.hit(player2)
        player2.hit(player1)
        print(f"{player1.name}: {player1.hitPoints} HP")
        print(f"{player2.name}: {player2.hitPoints} HP")
        print("")
        
        if player1.hitPoints <= 0:
            print("You lose.")
            keepGoing = False
        elif player2.hitPoints <= 0:
            print("You win!")
            keepGoing = False
        else:
            while choice:
                action = input("Do you want to fight or heal? ").lower()
                if action == "fight":
                    keepGoing = True
                    choice = False
                elif action == "heal":
                    player1.heal()
                    print(f"{player1.name} healed! Current HP: {player1.hitPoints}")
                    keepGoing = True
                    choice = False
                elif action == "f":
                    keepGoing = True
                    choice = False
                elif action == "h":
                    player1.heal()
                    print(f"{player1.name} healed! Current HP: {player1.hitPoints}")
                    keepGoing = True
                    choice = False
                else:
                    print("Invalid choice. Please enter 'fight' to fight or 'heal' to heal.")
                            

            user = input("Press ENTER for another round! ")
            print("")