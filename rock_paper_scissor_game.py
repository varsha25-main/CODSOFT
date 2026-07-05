import random
def play_game():
    while True:
        user_chc = input("Enter your choice ('Rock, Scissors, Paper'):").lower()
        print("--------------------------")
        print("Rule for playing this game !!!\n\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock")
        print("--------------------------") 
        computer_chc = random.choice(['rock', 'scissors', 'paper'])
        print()
        print(f"Computer's choice: {computer_chc}")
        user_score = 0
        computer_score = 0
        if user_chc == computer_chc:
            print("it's a tie!")
        elif ((user_chc == "rock" and computer_chc == "scissors") or 
        (user_chc == "scissors" and computer_chc == "paper") or
        (user_chc == "paper" and computer_chc == "rock")):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "no":
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

play_game()
