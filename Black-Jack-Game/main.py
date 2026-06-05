import random

def deal_cards():
    """ Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ take a list of cards and return a total score calculated """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return " Game Draw"
    elif c_score == 0:
        return " You lose, component has a Black Jack"
    elif u_score == 0:
        return " You win, You have a Black Jack"
    elif u_score > 21:
        return "You lose, You went over"
    elif c_score > 21:
        return "You win, Component went over"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"




def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        # this while loop maily works for the user cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} , Your score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else  :
            user_deal = input("Type 'yes' if u want to draw another card else type 'no' \n").lower()
            if user_deal == 'yes':
                user_cards.append(deal_cards())
            else:
                game_over = True



    while computer_score != 0 and computer_score<17:
        # this while loop works for the computer cards
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards} , Your final score: {user_score}")
    print(f"Computer final cards: {computer_cards} , final score: {computer_score}")
    print(compare(u_score = user_score, c_score = computer_score))

while (input("Do you want to play the Black Jack Game? Type 'yes' or 'no' \n").lower()) == "yes":
    print("\n" *50)
    play_game()