import random
print("lets play!")
options = ["rock","paper","scissors"]
running = True
score_player= 0
score_computer = 0
rounds =0

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
     player= input("Enter a choice from (rock,paper,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")
    
    if player == computer:
     print("It's a tie!")
     score_player=0
     score_computer= 0
    elif player =="rock" and computer =="scissors":
     print("you win!")
     score_player +=1
    elif player=="paper" and computer == "rock":
     print("you win!")
     score_player +=1
    elif player == "scissors" and computer == "paper":
     print("you win!")
     score_player +=1
    else:
     print("you lose!")
     score_computer +=1
    rounds += 1
    print(f"player wins:{score_player},computer wins:{score_computer},total rounds:{rounds}")
    print()
    play_again =input ("Play again? (y/n):").lower()
    if not play_again =="y":
        running = False
print("Thanks for playing")



     
