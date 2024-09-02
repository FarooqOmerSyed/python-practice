from dataclasses import dataclass, field
from typing import List, Dict

# Define a Player class with name and position attributes
@dataclass
class Player:
    name: str
    position: str

# Define a Team class with name and a list of players
@dataclass
class Team:
    name: str
    players: List[Player] = field(default_factory=list)

# Define a TeamRoster class to manage multiple teams
class TeamRoster:
    def __init__(self):
        # Initialize an empty dictionary to store teams
        self.teams: Dict[str, Team] = {}

    # Method to create a new team
    def create_team(self, team_name: str):
        if team_name in self.teams:
            print(f"Team {team_name} already exists.")
        else:
            self.teams[team_name] = Team(name=team_name)
            print(f"Team {team_name} created.")

    # Method to add a player to a specific team
    def add_player(self, team_name: str, player_name: str, player_position: str):
        if team_name not in self.teams:
            print(f"Team {team_name} does not exist.")
        else:
            player = Player(name=player_name, position=player_position)
            self.teams[team_name].players.append(player)
            print(f"Player {player_name} added to team {team_name}.")

    # Method to get and print the list of players from a specific team
    def get_team_players(self, team_name: str):
        if team_name not in self.teams:
            print(f"Team {team_name} does not exist.")
        else:
            team = self.teams[team_name]
            if not team.players:
                print(f"No players in team {team_name}.")
            else:
                print(f"Players in team {team_name}:")
                for player in team.players:
                    print(f"- {player.name} ({player.position})")

# Example usage
if __name__ == "__main__":
    roster = TeamRoster()
    
    while True:
        # Prompt the user to choose an action
        action = input("Choose an action: create_team, add_player, get_team_players, or quit: ").strip()
        
        if action == "create_team":
            # Create a new team
            team_name = input("Enter team name: ").strip()
            roster.create_team(team_name)
        
        elif action == "add_player":
            # Add a player to a specific team
            team_name = input("Enter team name: ").strip()
            player_name = input("Enter player name: ").strip()
            player_position = input("Enter player position: ").strip()
            roster.add_player(team_name, player_name, player_position)
        
        elif action == "get_team_players":
            # Get and print the list of players from a specific team
            team_name = input("Enter team name: ").strip()
            roster.get_team_players(team_name)
        
        elif action == "quit":
            # Exit the loop and end the program
            break
        
        else:
            print("Invalid action. Please try again.")
