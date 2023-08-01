"""
Tournament  winner

There's an algorithms tournament taking place in which teams of programmers
compete against each other to solve algorithimic problems as 
faster as possible. Teams compete in a round robin, where
each team faces off against all other teams. Only two teams compete
against each other at a time, and for each competition,
one team is designated the home team, while the other team is the away team.

In each competition there's always one winner and one lose;
ther are no ties. A team receives 3 points if it wins and 0 if it loses.
The winner of the tournament is the team that recieves the most amount of points


"""

def tournament_winner(competions, results):
    dict = {}

    for i, comp in enumerate(competions):
        if results[i]:
            dict[comp[0]] = dict.get(comp[0], 0) + 1
        else:
            dict[comp[1]] = dict.get(comp[1], 0) + 1

    return max(dict, key=dict.get)