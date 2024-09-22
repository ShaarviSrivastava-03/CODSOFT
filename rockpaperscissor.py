import random

def winner(optbyuser, optbycomp):       #function to know winner
    if optbyuser==optbycomp :            #when both have same choice
        return "It's a tie!"
    elif (optbyuser == "Rock" and optbycomp == "Scissors") or (optbyuser == "Scissors" and optbycomp == "Paper") or (optbyuser == "Paper" and optbycomp == "Rock"):
        return "You win!"                   #when you win
    else:                                    
        return "You lose!"                    #when uh lose

def playgame():
    choices = ["Rock","Paper", "Scissors"]
    optbyuser = input("Enter your choice (Rock, Paper, or Scissors): ") #taking user choice as input
    while optbyuser not in choices:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        optbyuser = input("Enter your choice: ")
    
    optbycomp = random.choice(choices)                               #choice randomly taken from the list
    print(f"You chose: {optbyuser}")
    print(f"Computer chose: {optbycomp}")
    
    result = winner(optbyuser,optbycomp)                      
    print(result)

playgame()

while True:
    play_again = input("Do you want to play again? (yes or no): ")            #to ask user as they want to play or not
    if play_again != "yes":
      break
    playgame()
