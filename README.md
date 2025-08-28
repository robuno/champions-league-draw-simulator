# UEFA Champions League League Phase Draw Simulator

This Python script simulates the new league phase draw for the UEFA Champions League, based on the format implemented in the 2024-2025 season. It provides a realistic experience by adhering to specific draw rules and, optionally, includes time delays to mimic a live ceremony.

## Features

- **Rule-Based Simulation:** The simulator strictly follows the official UEFA rules for the league phase draw.
  - Each team is matched with **8 different opponents**.
  - A team is **not matched** against any other team from its own pot.
  - A team is **not matched** against another team from the same country.
- **Customizable:** All team and pot information is read from an external text file (`teams.txt`), making it easy to update the data for future seasons without changing the code.
- **Interactive Experience:** The user can choose to enable or disable time delays.
  - With delays, the draw for each team is revealed one by one, adding a realistic, suspenseful element.
  - Without delays, the results are displayed instantly.

## How to Use

### 1. Create the Teams File

First, you need to create a plain text file named `teams.txt` in the same directory as the Python script. The file must contain the teams and their countries, with an empty line separating each pot.

### 2. Run the Script

Once the `teams.txt` file is ready, you can run the Python script from your terminal