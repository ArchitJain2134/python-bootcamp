from game_data import data
import random

final_score = 0
def format_data(account):
    """Format the account data into printable format"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b 
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print("vs") 
    print(f"Compare B: {format_data(account_b)}")

# ask the user to guess which account has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        final_score += 1
        print(f"You're right! Current score: {final_score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {final_score}.")
        game_should_continue = False