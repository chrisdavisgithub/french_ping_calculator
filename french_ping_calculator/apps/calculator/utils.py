"""Match and competition's result class"""
from calculator.constants import SCORE_TABLE


class Match(object):

    def __init__(self, player_point, opponent_point, is_won, coef):
        self.player_point = player_point
        self.opponent_point = opponent_point
        self.is_won = is_won
        self.coef = coef

    def outcomes_type(self):
        if self.player_point < self.opponent_point and self.is_won == "yes":
            return "UNEXPECTED_WINS"
        if self.player_point >= self.opponent_point and self.is_won == "yes":
            return "EXPECTED_WINS"
        if self.player_point <= self.opponent_point and self.is_won == "no":
            return "EXPECTED_LOSSES"
        if self.player_point > self.opponent_point and self.is_won == "no":
            return "UNEXPECTED_LOSSES"

    def get_result(self):
        point_difference = list(
            x for x in SCORE_TABLE.keys() if abs(self.player_point - self.opponent_point) in range(x[0], x[1])
        )
        return SCORE_TABLE.get(point_difference[0]).get(self.outcomes_type()) * float(self.coef)
        

class Competition(object):
    def __init__(self):
        self.matchs = []
        self.result = 0

    def get_result(self):
        for match in self.matchs:
            self.result += match.get_result()
        return self.result

