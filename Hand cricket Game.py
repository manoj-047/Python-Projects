import random

def get_valid_input(prompt, input_type=str, valid_options=None, min_value=None, max_value=None):
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if input_type == int:
                user_input = int(user_input)
                if min_value is not None and user_input < min_value:
                    print(f"Please enter a number greater than or equal to {min_value}")
                    continue
                if max_value is not None and user_input > max_value:
                    print(f"Please enter a number less than or equal to {max_value}")
                    continue
            if valid_options and user_input not in valid_options:
                print(f"Please enter one of these options: {', '.join(valid_options)}")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def toss():
    print("\nToss Time!")
    user_choice = get_valid_input("Choose Odd or Even (O/E): ", valid_options=['o', 'e'])
    user_num = get_valid_input("Enter your number (1-6): ", input_type=int, min_value=1, max_value=6)
    
    opponent_num = random.randint(1, 6)
    total = user_num + opponent_num
    print(f"\nYour number: {user_num}, Opponent's number: {opponent_num}")
    print(f"Total: {total} -> {'Even' if total % 2 == 0 else 'Odd'}")

    if (total % 2 == 0 and user_choice == 'e') or (total % 2 != 0 and user_choice == 'o'):
        print("You won the toss!")
        print("-----------------")
        decision = get_valid_input("\nBatting or Bowling? (bat/bowl): ", valid_options=['bat', 'bowl'])
        return 'user', decision
    else:
        print("\nOpponent won the toss!")
        print("------------------------")
        decision = random.choice(['bat', 'bowl'])
        print(f"Opponent chooses to {decision}")
        return 'opponent', decision

def play_innings(batting_side):
    score = 0
    print("\n-------------------------")
    print(f"{'You' if batting_side == 'user' else 'Opponent'} is batting!")
    print("-------------------------")
    
    while True:
        if batting_side == 'user':
            user_num = get_valid_input("\nYour turn (1-6): ", input_type=int, min_value=1, max_value=6)
            opponent_num = random.randint(1, 6)
            print(f"You played: {user_num}")
            print(f"Opponent bowled: {opponent_num}")
        else:
            opponent_num = get_valid_input("\nYour bowling (1-6): ", input_type=int, min_value=1, max_value=6)
            user_num = random.randint(1, 6)
            print(f"Opponent played: {user_num}")
            print(f"You bowled: {opponent_num}")
        
        if user_num == opponent_num:
            print("\nOUT! Innings Over!")
            print("------------------")
            break
        else:
            score += user_num
            print(f"Current Score: {score}")
    
    return score

def display_result(user_score, opponent_score):
    print("\n====== FINAL SCORE ======")
    print(f"You: {user_score}")
    print(f"Opponent: {opponent_score}")
    print("========================")
    
    if user_score > opponent_score:
        print("\n🎉 Congratulations! You won!")
    elif user_score < opponent_score:
        print("\n😢 Opponent won!")
    else:
        print("\n🤝 It's a tie!")

def main():
    print("==========================")
    print("   HAND CRICKET GAME      ")
    print("==========================")
    
    # Initialize scores
    user_score = 0
    opponent_score = 0
    
    toss_winner, decision = toss()

    if toss_winner == 'user':
        if decision == 'bat':
            user_score = play_innings('user')
            opponent_score = play_innings('opponent')
        else:
            opponent_score = play_innings('opponent')
            user_score = play_innings('user')
    else:
        if decision == 'bat':
            opponent_score = play_innings('opponent')
            user_score = play_innings('user')
        else:
            user_score = play_innings('user')
            opponent_score = play_innings('opponent')

    display_result(user_score, opponent_score)
    
    play_again = get_valid_input("\nPlay again? (yes/no): ", valid_options=['yes', 'no'])
    if play_again == 'yes':
        main()
    else:
        print("\nThanks for playing!")

if __name__ == "__main__":
    main()
