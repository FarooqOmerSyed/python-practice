from typing import List
from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)

    def add_member(self, member: str):
        self.members.append(member)

    def print_members(self):
        print(f"Team {self.name} has the following members:")
        for member in self.members:
            print(member)

# Create a team instance
team_name = input("Enter the team name: ")
team = Team(name=team_name)

# Ask the user to add members to the team
while True:
    member_name = input("Enter a member's name (or type 'done' to finish): ")
    if member_name.lower() == 'done':
        break
    team.add_member(member_name)

# Print the members of the team
team.print_members()
