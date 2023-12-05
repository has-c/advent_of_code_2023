
if __name__ == "__main__":

    puzzle_input_path = r"C:\Users\hcheena\OneDrive - Quantium\Documents\Repos Copy\adhoc_scripts\advent_of_code_2023\Day_2\day_2_puzzle.txt"
    num_cubes = {'red':12,'green':13,'blue':14}
    
    # Part 1
    impossible_games = []
    all_games = []
    with open(puzzle_input_path, 'r') as file:
        # Read each line
        for line in file:
            # Process game
            game_id, games = line.strip().split(":")
            game_id = int(game_id.split(" ")[1])
            all_games.append(game_id)
            games = games.split(";")
            for game in games:
                cubes_played = game.strip().split(", ")
                for cube in cubes_played:
                    num, colour = cube.split(" ")
                    if int(num) > num_cubes[colour.lower()]:
                        impossible_games.append(game_id)
                        # go to next game
                        break

    possible_games = set(all_games).difference(set(impossible_games))
    print(sum(possible_games))

    # Part 2
    powers = []
    with open(puzzle_input_path, 'r') as file:
        # Read each line
        for line in file:
            # Process game
            game_id, games = line.strip().split(":")
            game_id = int(game_id.split(" ")[1])
            all_games.append(game_id)
            games = games.split(";")
            fewest_cubes = {'red':0,'green':0,'blue':0}
            for game in games:
                cubes_played = game.strip().split(", ")
                for cube in cubes_played:
                    num, colour = cube.split(" ")
                    if fewest_cubes[colour] < int(num):
                        fewest_cubes[colour] = int(num)
            
            # Fewest cubes required for this game calculated
            # Now get power set
            fewest_cubes = list(fewest_cubes.values())
            power = fewest_cubes[0] * fewest_cubes[1] * fewest_cubes[2]
            powers.append(power)

    print(sum(powers))