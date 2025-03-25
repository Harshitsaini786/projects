import random

print("\t\t\t\tWelcome to the game of strong,paper,scissor\t\t\t\t")
a=1
b=2
c=3
computer_score=0
user_score=0

def user_choice(user_decision):
    if user_decision==a:
        print("user choose strong")
    elif user_decision==b:
        print("user choose paper")
    elif user_decision==c:
        print("user choose scissor")
    else:
        print("invalid input")

def computer_choice(computer_decision):
    if computer_decision==a:
        print("computer choose strong")
    elif computer_decision==b:
        print("computer choose paper")
    elif computer_decision==c:
        print("computer choose scissor")
    else:
        print("invalid input")
def game(user_decision,computer_decision):
    global computer_score,user_score
    if user_decision==a and computer_decision==b:
      computer_score+=1
      print("computer wins")
    elif user_decision==b and computer_decision==c:
      computer_score+=1
      print("computer wins")
    elif user_decision==c and computer_decision==a:
      computer_score+=1
      print("computer wins")
    elif user_decision==computer_decision:
      print("tie") 
    else:
      user_score+=1
      print("user wins")

def Rounds():
   global user_score, computer_score
   try:
       total_rounds = int(input("Enter the number of rounds you want to play: "))
       if total_rounds <= 0:
           print("Number of rounds must be greater than 0. Exiting game.")
           return
   except ValueError:
       print("Invalid input. Please enter a valid number. Exiting game.")
       return

   for i in range(total_rounds):
       print(f"\nRound {i + 1}")
       user_decision = int(input("choose strong=1,paper=2,scissor=3 for your turn: "))
       while user_decision not in [a, b, c]:
           print("invalid input")
           user_decision = int(input("choose strong=1,paper=2,scissor=3 for your turn: "))
       computer_decision = random.choice([a, b, c])
       user_choice(user_decision)
       computer_choice(computer_decision)    
       game(user_decision, computer_decision)
       print("user score is", user_score)
       print("computer score is", computer_score)

   print("\nFinal Results:")
   if user_score > computer_score:
       print("User is the overall winner!")
   elif user_score < computer_score:
       print("Computer is the overall winner!")
   else:
       print("The game is a tie!")
   print(f"Final Scores - User: {user_score}, Computer: {computer_score}")  

Rounds()

print("Thanks for playing the game")