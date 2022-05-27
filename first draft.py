import random
#Assigning cards and totals to variables
card_a = random.randint(1, 13)
card_b = random.randint(1, 13)
card_total = 0
if card_a > 10:
    card_a = 10
if card_b > 10:
    card_b = 10
print(f"You have the cards {card_a}, {card_b}")
card_total = card_a + card_b
h_or_s = input("Do you want to hit or stand (H or S): ")
#Checks to see if hitting or standing and then will generate a new card and give current total while checking if below 21
if h_or_s.lower() == "h":
    new_card = random.randint(1,13)
    if new_card > 10:
        new_card = 10
    card_total += new_card
    print(f"You have now been dealt {new_card}")
    if card_total > 21:
        print(f"You have Bust! Your total is {card_total}")
    elif card_total == 21:
        print("BlackJack! Your total is 21")
    else:
        print(f"Your new total is {card_total}")
elif h_or_s =="s":
    print(f"Your Total is {card_total}")