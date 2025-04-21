import random
import time

# Snakes and ladders positions
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# Player positions
player_positions = {
    "Player 1": 0,
    "Player 2": 0
}

def roll_dice():
    return random.randint(1, 6)

def move_player(player, roll):
    print(f"{player} rolled a {roll}")
    start = player_positions[player]
    end = start + roll

    if end > 100:
        print(f"{player} needs exactly {100 - start} to win. Stay at {start}.")
        return

    print(f"{player} moves from {start} to {end}")

    if end in snakes:
        print(f"Oops! {player} landed on a snake! Slither down to {snakes[end]}")
        end = snakes[end]
    elif end in ladders:
        print(f"Yay! {player} found a ladder! Climb up to {ladders[end]}")
        end = ladders[end]

    player_positions[player] = end

def check_winner(player):
    return player_positions[player] == 100

def play_game():
    print("Welcome to Snake and Ladder!")
    print("First to reach 100 wins!\n")

    players = list(player_positions.keys())
    turn = 0

    while True:
        current_player = players[turn % 2]
        input(f"{current_player}, press Enter to roll the dice...")
        dice = roll_dice()
        move_player(current_player, dice)

        print(f"{current_player} is now at {player_positions[current_player]}\n")

        if check_winner(current_player):
            print(f"🎉🎉 {current_player} wins! 🎉🎉")
            break

        turn += 1
        time.sleep(1)

if __name__ == "__main__":
    play_game()
