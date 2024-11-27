from enum import Enum
from abc import ABC, abstractclassmethod

class Teams(Enum):
    TEAM_RED = 1
    TEAM_GREEN = 2
    TEAM_BLUE = 3

class TeamMembershipLookUp:
    @abstractclassmethod
    def find_all_students(self, team):
        pass

class Student:
    def __init__(self, name) -> None:
        self.name = name

class TeamMemberShips(TeamMembershipLookUp):
    def __init__(self) -> None:
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students(self, team):
        for member in self.team_memberships:
            if member[1] == team:
                yield member[0].name

class Analysis:
    def __init__(self, team_membership_lookup) -> None:
       for student in team_membership_lookup.find_all_students(Teams.TEAM_RED):
        print(f"{student} is in RED team")

student_01 = Student("Mykhailo")
student_02 = Student("Michael")
student_03 = Student("Mike")

team_memberships = TeamMemberShips()
team_memberships.add_team_memberships(student_01, Teams.TEAM_RED)
team_memberships.add_team_memberships(student_02, Teams.TEAM_RED)
team_memberships.add_team_memberships(student_03, Teams.TEAM_RED)

Analysis(team_memberships)
