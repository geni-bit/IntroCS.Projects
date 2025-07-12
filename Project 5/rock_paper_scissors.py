#improting the random function 
import random

def RPS_game():
    """The function RPS game is a program that simulates a round of rock-paper-scissors,
    with the user playing against the computer""" 
    #the computer will choose an option at random from the following choices of rock, paper, and scissors
    comp_choice = random.choice(["rock", "paper", "scissors"])
    #the player to choice an option from following choices of rock, paper, and scissors
    player_choice = input("Choose rock, paper, or scissors: ")
    #To make sure the player is choosing from the following options and not something else
    if not (is_legal(player_choice)):
        print("You must select from rock, paper, or scissors")
    else:
        #printing out the computer's choice 
        print("The computer chose", comp_choice)
        #if the player's choice beats the computer's choice, then it will print out, "You win" to the player
        if beats(player_choice, comp_choice):
            print("You win!")
        #if the computer's choice beats the player's choice, then it will print out, "You lost" to the player
        elif beats(comp_choice, player_choice):
            print("You lost. :(")
        #anything else happens besides the other if statements above
        #the the computer's amd the player's choices are the same, then it will print out, "It's a tie" to the player
        else:
            print("It's a tie.")

def is_legal(choice:str) -> bool:
    """The function (is_legal) is to check if weapons chosen by the
    user and computer are either “rock”, “paper”, or “scissors"""
    #if the player choices from either rock, paper, or scissors, then it will return true 
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    #if the player doesn't choice from any of the choices, then it will return False 
    else:
        return False
    
def beats(weapon1:str,weapon2:str) -> bool:
    """The function (beats) takes in  the weapons from two players and determines if the weapon
    chosen by the first players beats the weapon chosen by the second player."""
    #Checking each of the player and computer weapons if they one these three outcomes, the it will return True 
    if (weapon1 == "rock" and weapon2 == "scissors") or (weapon1 == "paper" and weapon2 == "rock") or (weapon1 == "scissors" and weapon2 == "paper"):
        return True
    #if anything else, the player and computer choices doesn't match any of the options then it will return False 
    else:
        return False

