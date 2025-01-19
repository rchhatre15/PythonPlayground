import random
play = input("Would you like to play blackjack (type 'y' or 'n'): ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    total = sum(cards)
    if total <= 21:
        return total
    elif cards.count(11) == 0:
        return total
    else:
        cards[cards.index(11)] = 1
        calculate_score(cards)

while play == "y":
    computer = []
    player = []

    # first draw
    for i in range(2):
        computer.append(cards[random.randint(0, 12)])
        player.append(cards[random.randint(0, 12)])
    
    print(f"Your Cards: {player}")
    print(f"Computer's first card: {computer[0]}")

    player_result = calculate_score(player)
    computer_result = calculate_score(computer)
    if player_result == 21:
        if computer_result == 21:
            print("You drew!")
        else:
            print("You win!")
    else:
        again = input("Type 'y' to get another card, type 'n' to pass:")
        while again == "y":
            player.append(cards[random.randint(0, 12)])
            print(f"Your Cards: {player}")
            player_result = calculate_score(player)
            if player_result == 21:
                print(f"Computer's Cards: {computer}")
                if computer_result == 21:
                    print("You drew!")
                elif computer_result > 16:
                    print("You win!")
                again = "n"
            elif player_result > 21:
                print(f"Computer's Cards: {computer}")
                computer_result = 21
                print("You sold.")
                again = "n"
            else:
                again = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if not computer_result == 21:
            computer_result = calculate_score(computer)
            while computer_result < 17:
                computer.append(cards[random.randint(0, 12)])
                computer_result = calculate_score(computer)
            print(f"Computer's Cards: {computer}")
            if computer_result > 21 or player_result > computer_result:
                print("You won!")
            elif computer_result == player_result:
                print("It's a draw!")
            else:
                print("You sold.")
        elif computer_result == 21 and player_result < computer_result:
            print(f"Computer's Cards: {computer}")
            print("You sold.")

    play = input("Would you like to play blackjack (type 'y' or 'n'): ")




