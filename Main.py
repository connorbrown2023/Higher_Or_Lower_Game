from Game_Data import data
import random

def check_answer(guess, a_account, b_account):
    """Takes guess, account a and then account b, and returns if the guess was right"""
    if a_account > b_account:
        return guess == "a"
    else:
        return guess == "b"


def format_data(account):
    """Takes account data and returns it in printable format"""
    account_name = account["Name"]
    account_description = account["Description"]
    account_country = account["Country"]
    return f"{account_name}, a {account_description} from {account_country}"


# Generate a random account from data file.
account_a = random.choice(data)
account_b = random.choice(data)
score = 0
should_game_go_on = True
account_b = random.choice(data)

# Use a while loop to make repeatable
while should_game_go_on:

    # Replacing position A with B in the printable format
    account_a = account_b
    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers A or B?").lower()



    # Check if user is correct.
    ## Get followers account size
    account_a_followers = account_a["Follower Count"]
    account_b_followers = account_b["Follower Count"]
    is_correct = check_answer(guess, account_a_followers, account_b_followers)

    # Give user feedback
    # Track their score
    if is_correct:
        score += 1
        print(f"Your Right!! your score is {score}\n\n")
    else:
        print(f"Your Wrong. your final score is {score}")
        # Check if user wants to play again
        play_again = input("Would you like to play again Y/N").lower()
        if play_again == "y":
            should_game_go_on = True
            score = 0
        else:
            should_game_go_on = False