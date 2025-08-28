import random
import time

def read_teams_from_file(filename="teams.txt"):
    """
    Reads team and country data from a text file and organizes it into pots and a dictionary.
    Returns a tuple containing the list of pots and the team-country dictionary.
    """
    pots = [[] for _ in range(4)]
    team_countries = {}
    current_pot_index = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    current_pot_index += 1
                    continue
                
                parts = line.split(',')
                team_name = parts[0].strip()
                country = parts[1].strip()
                
                pots[current_pot_index].append(team_name)
                team_countries[team_name] = country
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None
    except IndexError:
        print(f"Error: Malformed line in the file '{filename}'. Please check the format.")
        return None, None

    return pots, team_countries

def simulate_draw():
    """
    Simulates the Champions League league phase draw with a user-selectable timer delay.
    """
    all_pots, team_countries = read_teams_from_file()

    if all_pots is None or team_countries is None:
        return # Exit if file reading failed

    all_teams = [team for pot in all_pots for team in pot]
    matches = {team: [] for team in all_teams}

    print("--- Welcome to the UEFA Champions League Draw Ceremony! 🏆 ---")
    
    use_delay = ""
    while use_delay.lower() not in ["yes", "no"]:
        use_delay = input("Would you like to use the timer delay for a more realistic experience? (yes/no): ")
        if use_delay.lower() not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")

    if use_delay.lower() == "yes":
        print("\nGet ready! The draw is about to begin...")
        time.sleep(2)
        
    for team in all_teams:
        print(f"\n--- Now drawing opponents for **{team}** ---")
        if use_delay.lower() == "yes":
            time.sleep(1)

        team_pot = [p for p in all_pots if team in p][0]
        
        opponent_pool = []
        for pot in all_pots:
            if pot is not team_pot:
                opponent_pool.extend(pot)
        
        eligible_opponents = [opponent for opponent in opponent_pool 
                              if team_countries.get(opponent) != team_countries.get(team)]

        if len(eligible_opponents) < 8:
            print(f"Error: Not enough eligible opponents for {team} to draw 8 unique teams. Skipping...")
            continue
        
        selected_opponents = random.sample(eligible_opponents, 8)
        matches[team] = selected_opponents
        
        if use_delay.lower() == "yes":
            print("The matchups are being determined by the system...")
            time.sleep(2)
            print(f"**{team}** will face:")
            for opponent in selected_opponents:
                print(f" - {opponent}")
                time.sleep(1)
        else:
            print(f"**{team}** will face these opponents: {', '.join(selected_opponents)}")
            
    print("\n--- The Draw Ceremony is Complete! ✨ ---")

# Run the simulation
simulate_draw()