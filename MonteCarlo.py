import random


def roll_dice():
    return random.randint(1, 6)


def play_dice(target_score):
    player_scores = [0, 0]  # Inicializace skóre pro 2 hráče
    current_player = 0     
    consecutive_six = 0

    while max(player_scores) < target_score:
        # Hod kostkou
        dice_roll = roll_dice()

       #Určení skóre dle hodu
        if dice_roll == 1:
            # Pokud hráč hodí jedničku, tak se jeho skóre resetuje a hraje další hráč
            player_scores[current_player] = 0
            current_player = 1 - current_player
        else:
            # Jinak se přičte ke skóre hráče hodnota kostky
            player_scores[current_player] += dice_roll

            if dice_roll == 6:
                consecutive_six += 1
                if consecutive_six == 2:
                    # Při hození hodnoty 6 vícekrát po sobě se skóre zresetuje a přepne se na dalšího hráče
                    player_scores[current_player] = 0
                    consecutive_six = 0
                    current_player = 1 - current_player
            else:
                consecutive_six = 0

    return current_player

# Cílové skóre hry
target_score = 50

# Simulace hry kostky pomocí metody Monte Carlo
num_simulations = 500
wins_player1 = 0
wins_player2 = 0
losses_player1 = 0
losses_player2 = 0

for i in range(num_simulations):
    winner = play_dice(target_score)
    if winner == 0:
        wins_player1 += 1
        losses_player2 += 1
    else:
        wins_player2 += 1
        losses_player1 += 1

# Výpočet pravděpodobnosti výhry pro jednotlivé hráče
probability_player1 = wins_player1 / num_simulations
probability_player2 = wins_player2 / num_simulations

print(f"Number of wins for Player 1: {wins_player1}")
print(f"Number of losses for Player 1: {losses_player1}")
print(f"Number of wins for Player 2: {wins_player2}")
print(f"Number of losses for Player 2: {losses_player2}")
print(f"Probability of Player 1 winning: {probability_player1}")
print(f"Probability of Player 2 winning: {probability_player2}")
