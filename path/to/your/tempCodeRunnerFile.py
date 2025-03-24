import random

print("\t\t\t\tWelcome to the game of Strong, Paper, Scissor\t\t\t\t")

a = 1
b = 2
c = 3
computer_score = 0
user_score = 0

def user_choice(user_decision):
    if user_decision == a:
        print("User chose Strong")
    elif user_decision == b:
        print("User chose Paper")
    elif user_decision == c:
        print("User chose Scissor")
    else:
        print("Invalid input")

def computer_choice(computer_decision):
    if computer_decision == a:
        print("Computer chose Strong")
    elif computer_decision == b:
        print("Computer chose Paper")
    elif computer_decision == c:
        print("Computer chose Scissor")
    else:
        print("Invalid input")

def game(user_decision, computer_decision):
    global computer_score, user_score  # Use global to modify the scores
    if user_decision == a and computer_decision == b:
        computer_score += 1
        print("Computer wins this round!")
    elif user_decision == b and computer_decision == c:
        computer_score += 1
        print("Computer wins this round!")
    elif user_decision == c and computer_decision == a:
        computer_score += 1
        print("Computer wins this round!")
    elif user_decision == computer_decision:
        print("It's a tie this round!")
    else:
        user_score += 1
        print("User wins this round!")

def Rounds(rounds):
    global user_score, computer_score  # Ensure scores are tracked globally
    for i in range(rounds):
        print(f"\nRound {i + 1}")
        user_decision = int(input("Choose Strong = 1, Paper = 2, Scissor = 3 for your turn: "))
        while user_decision not in [a, b, c]:
            print("Invalid input. Please try again.")
            user_decision = int(input("Choose Strong = 1, Paper = 2, Scissor = 3 for your turn: "))
        
        computer_decision = random.choice([a, b, c])

        # Display choices
        user_choice(user_decision)
        computer_choice(computer_decision)

        # Determine the winner of the round
        game(user_decision, computer_decision)
        print(f"User Score: {user_score} | Computer Score: {computer_score}")

    # Determine the winner after all rounds
    print("\nFinal Score:")
    print(f"User Score: {user_score} | Computer Score: {computer_score}")
    if user_score > computer_score:
        print("User wins the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

# Play 3 rounds
Rounds(3)

print("Thanks for playing the game!")
