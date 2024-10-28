import random

def player_entry():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players > 0:
                num_players += 1
                break
            else:
                print("Invalid number of players, please choose 1 or more players.")
        except ValueError:
            print("Invalid input, enter a number.")
    bet_type = None
    bet_value = None
    wager = 0
    balance = 1000
    player_storage = []
    for x in range(1, num_players):
        player_storage.append([x,bet_type, bet_value, wager, balance])
    return num_players, player_storage
    
def menu(num_players, player_storage):
    num_players -= 1
    for players in range(0, num_players, 1):
        if player_storage[players][4] > 0:
            print(f"\n\t\t\tSic Bo")
            print("----------------------------------------------------------------------")
            print(f"Player {player_storage[players][0]}, Please make a selection from the choices below.")
            print("----------------------------------------------------------------------")
            bet_info()
            print("\n")
            valid_bet = ["1", "big", "2", "small", "3", "specifictriple", "4", "anytriple", "5", "specificdouble", "6", "total"]
            while True:
                try:
                    bet_type = input("Enter your bet type (1. Big, 2. Small, 3. Specific Triple, 4. Any Triple, 5. Specific Double, 6. Total): ").replace(" ", "").lower()
                    if bet_type in valid_bet:
                        break
                    else:
                        print("Invalid bet type. Please try again.")
                except ValueError:
                    print("Invalid input. Enter a number in the form of an integer.")
            player_storage[players][1] = bet_type
            bet_value = None
            while True:
                try:
                    if bet_type in ["3", "specifictriple", "5", "specificdouble"]:
                        while True:
                            bet_value = int(input("Enter the number you'd like to bet on: "))
                            if bet_value >= 1 and bet_value <= 6:
                                break
                            else:
                                print("Invalid selection, pick a number between 1 and 6.")
                        player_storage[players][2] = bet_value
                    elif bet_type in ["6", "total"]:
                        while True:
                            bet_value = int(input("Enter the number you'd like to bet on: "))
                            if bet_value >= 3 and bet_value <= 18:
                                break
                            else:
                                print("Invalid total, please pick a number between 3 and 18")
                        player_storage[players][2] = bet_value
                    break
                except ValueError:
                    print("Invalid input, please enter a number.")
            while True:
                try:
                    wager = float(input("Enter how much you would like to bet: "))
                    if wager <= player_storage[players][4] and player_storage[players][4] > 0 and wager > 0:
                        break
                    else:
                        print("Your balance is not sufficient to make that bet or you entered an invalid wager. Please try again.")
                except ValueError:
                    print("Invalid input, enter a number.")
            player_storage[players][3] = wager
        else:
            print(f"Player {player_storage[players][0]}, you have no money.")
    return player_storage
                
def roll_dice():
        dice = [random.randint(1, 6) for _ in range(3)]
        print(f"Dice: {dice}")
        return dice

def bet_check(bet_type, bet_value, dice):
    total = sum(dice)
    unique_dice = set(dice)
    #print(bet_type)
    if bet_type == "big" or bet_type == "1":
        return 11 <= total <= 17 and len(unique_dice) != 1  # Excludes triples
        #print("big")
    elif bet_type == "small" or bet_type == "2":
        return 4 <= total <= 10 and len(unique_dice) != 1  # Excludes triples
    elif bet_type == "specifictriple" or bet_type == "3":
        return dice[0] == dice[1] == dice[2] == bet_value
    elif bet_type == "anytriple" or bet_type == "4":
        return len(unique_dice) == 1
    elif bet_type == "specificdouble" or bet_type == "5":
        return list(dice).count(bet_value) >= 2
    elif bet_type == "total" or bet_type == "6":
        return total == bet_value
    return False

def bet_info():
    print("\n---------------------------------------------------------------------------------------------------------------------------")
    print("Big: Betting that the total of the three dice will be between 11 and 17 (no triples). House Edge - 2.78% - Odds - 1:1\n")
    print("Small: Betting that the total of the three dice will be between 4 and 10 (no triples). House Edge - 2.78% - Odds - 1:1\n")
    print("Specific triple: Betting that all three dice will land on a specific number (three of selected number). House Edge - 16.2% - Odds - 150:1\n")
    print("Any triple: Betting that all three dice will land on the same number (any three of the same number). House Edge - 13.89% - Odds - 24:1\n")
    print("Specific double: Betting that two out of the three dice will land on a specific number. House Edge - 18.52% - Odds - 8:1\n")
    print("Total: Betting on the sum of the three dice. House edge - 20% - Odds - 30:1")
    print("---------------------------------------------------------------------------------------------------------------------------\n")

def profit_calc(player_storage, player):
    bet_type = player_storage[player][1]
    wager = player_storage[player][3]
    profit = 0
    if bet_type == "big" or bet_type == "1":
        profit = wager
        profit = profit - (profit * 0.0278)
    elif bet_type == "small" or bet_type == "2":
        profit = wager
        profit = profit - (profit * 0.0278)
    elif bet_type == "specifictriple" or bet_type == "3":
        profit = wager * 150
        profit = profit - (profit * 0.162)
    elif bet_type == "anytriple" or bet_type == "4":
        profit = wager * 24
        profit = profit - (profit * 0.1389)
    elif bet_type == "specificdouble" or bet_type == "5":
        profit = wager * 8
        profit = profit - (profit * 0.1852)
    elif bet_type == "total" or bet_type == "6":
        profit = wager * 30
        profit = profit - (profit * 0.2)
    return profit

def player_stats(player_storage):
    players_have_money = False
    for player in player_storage:
        print("---------------------------------")
        print(f"Player {player[0]}")
        print(f"Your balance is ${player[4]:.2f}")
        if player[4] > 0:
            players_have_money = True
    print("---------------------------------")
    if players_have_money:
        continuation()
    else:
        print("All players are out of money. Game Over.")
        exit()

def continuation():
    valid_entry = ["y","yes","n","no"]
    while True:
        try:
            entry = input("Would you like to continue? Y/N: ").strip().lower()
            if entry in valid_entry:
                if entry == "y" or entry == "yes":
                    break
                else:
                    print("Thanks for playing!")
                    exit()
            else:
                print("Error, enter Y/N or Yes/No")
                pass
        except ValueError:
            print("Error, enter Y/N or Yes/No")
def results(player_storage, num_players, dice):
    for player in range(num_players-1):
        if player_storage[player][4] > 0:
            if bet_check(player_storage[player][1],player_storage[player][2],dice):
                profit = profit_calc(player_storage,player)
                player_storage[player][4] += profit
                print(f"Congratulations Player {player_storage[player][0]}, you won ${profit:.2f}!")
                player_storage[player][4] = round(player_storage[player][4], 2)
            else:
                print(f"Sorry, Player {player_storage[player][0]}, You Lost!")
                player_storage[player][4] -= player_storage[player][3]
                player_storage[player][4] = round(player_storage[player][4], 2)
        else:
            print(f"Player {player_storage[player][0]} is out of the game.")
    
def main():
    num_players, player_storage = player_entry()
    while True:
        menu(num_players, player_storage)
        dice = roll_dice()
        results(player_storage, num_players, dice)
        player_stats(player_storage)
main()
