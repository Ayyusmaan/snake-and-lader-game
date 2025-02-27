import random


snakes = {15: 5, 22: 17}
ladders = {3: 19, 7: 35}

player_positions = [0, 0]
current_player = 0  

while True:
    input(f"Player {current_player + 1}, press Enter to roll the dice...")
    
    dice_roll = random.randint(1, 6)
    print(f"Player {current_player + 1} rolled a {dice_roll}")
    
    old_position = player_positions[current_player]
    new_position = old_position + dice_roll
    
    if new_position > 100:
        new_position = old_position 
        print(f"Can't move! Stay at position {old_position}")
    else:
        if new_position in ladders:
            print(f"Yay! Climbed ladder from {new_position} to {ladders[new_position]}")
            new_position = ladders[new_position]
        elif new_position in snakes:
            print(f"Oops! Snake bite! Fell from {new_position} to {snakes[new_position]}")
            new_position = snakes[new_position]
        
        player_positions[current_player] = new_position
        print(f"Player {current_player + 1} moved to position {new_position}")
    
    if new_position == 100:
        print(f"\n Player {current_player + 1} wins! ")
        break
    
    current_player = 1 - current_player
    print("\n" + "-"*30 + "\n")
