import random
def generate_card(): #Generates a random number and assigns a suit and face name
    x = random.randint(1, 13)
    y = random.randint(1, 4)
    if x == 1:
        x = "A"
    elif x == 10:
        x = "T"
    elif x == 11:
        x = "J"
    elif x == 12:
        x = "Q"
    elif x == 13:
        x = "K"
    if y == 1:
        y = "h"
    elif y == 2:
        y = "s"
    elif y == 3:
        y = "d"
    elif y == 4:
        y = "c"
    return str(x) + str(y)
def check_card_value(card):
    if card[0] == "2" or card[0] == "3" or card[0] == "4" or card[0] == "5" or card[0] == "6" or card[0] == "7" or card[0] == "8" or card[0] == "9":
       total_value = int(card[0])
    elif card[0] == "A":
        total_value = 11
    else:
        total_value = 10
    return total_value
def deal_two_cards_with_value():
    card_one = generate_card()
    card_two = generate_card()
    while card_two == card_one:
        print("rerolling")
        card_two = generate_card()
    card_value = check_card_value(card_one) + check_card_value(card_two)
    hand =f"| {card_one} | {card_two} |"
    print(hand)
    if card_value == 21:
        print("|B|L|A|C|K|J|A|C|K|")
    elif card_one[0] == "A" or card_two[0] == "A":
        print(f"Card Value = {card_value - 10} or {card_value}")
    elif card_one[0] =="A" and card_two[0] == "A":
        print(f"Card Value = {card_value - 20} or {card_value - 10}")
    else:
        print(f"Card Value = {card_value}")

deal_two_cards_with_value()