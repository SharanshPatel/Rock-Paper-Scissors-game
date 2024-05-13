import random

user_wins = 0
computer_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors to pick  OR  Q for quite: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_picks = options[random_number]
    print("computer picked",computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissors":
        print ("You won")
        user_wins += 1


    elif user_input == "paper" and computer_picks == "rock":
        print ("You won")
        user_wins += 1
  

    elif user_input == "scissors" and computer_picks == "paper":
        print ("You won")
        user_wins += 1

    elif user_input == "scissors" and computer_picks == "scissors":
        print ("It's a draw")
        draw += 1
    
    elif user_input == "paper" and computer_picks == "paper":
        print ("It's a draw")
        draw += 1
    
    elif user_input == "rock" and computer_picks == "rock":
        print ("It's a draw")
        draw += 1

    else:
        print ("You Loss! ")
        computer_wins += 1

print ("You won  =", user_wins, "times.")
print ("You lost =",computer_wins, "times.")
print ("You draw =", draw, "times.")
print("Goodbey !")        

