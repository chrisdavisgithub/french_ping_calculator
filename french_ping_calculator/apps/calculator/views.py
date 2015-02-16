from django.http import HttpResponseRedirect
from django.shortcuts import render

from calculator.constants import SCORE_TABLE
from calculator.forms import MatchForm
from calculator.forms import PlayerForm
from django.forms.formsets import formset_factory


class Match(object):

    def __init__(self, player_point, opponent_point, is_won, coef):
        self.player_point = player_point
        self.opponent_point = opponent_point
        self.coef = coef
        self.is_won = is_won

    def outcomes_type(self):
        if self.player_point < self.opponent_point and self.is_won == "yes":
            return "anormal_victory"
        if self.player_point >= self.opponent_point and self.is_won == "yes":
            return "normal_victory"
        if self.player_point <= self.opponent_point and self.is_won == "no":
            return "normal_defeat"
        if self.player_point > self.opponent_point and self.is_won == "no":
            return "anormal_defeat"

    def get_result(self):
        point_difference = list(
            x for x in SCORE_TABLE.keys() if abs(self.player_point - self.opponent_point) in range(x[0], x[1])
        )
        return SCORE_TABLE[point_difference[0]][self.outcomes_type()] * float(self.coef)


class Competition(object):
    def __init__(self,):
        self.matchs = []
        self.result = 0

    def get_result(self):
        for match in self.matchs:
            self.result += match.get_result()
        return self.result


def PingCalculatorView(request):
    match_formset = formset_factory(MatchForm, max_num=5)
    player_form = PlayerForm(prefix='player')
    if request.method == 'POST':
        match_formset = match_formset(request.POST, request.FILES, prefix='match')
        player_form = PlayerForm(request.POST, request.FILES, prefix='player')
        if match_formset.is_valid() and player_form.is_valid():
            competition = Competition()
            for form in match_formset.cleaned_data:
                player_point = player_form.cleaned_data.get('player_point')
                match = Match(player_point=player_point, **form)
                competition.matchs.append(match)
            return render(request, 'ping_calculator.html', {
                'match_formset': match_formset,
                'player_form': player_form,
                "competition": competition
            })
        else:
            return render(request, 'ping_calculator.html', {
                'match_formset': match_formset,
                'player_form': player_form,
            })
    elif request.method == 'GET':
        return render(request, 'ping_calculator.html', {
            'match_formset': match_formset(prefix='match'),
            'player_form': player_form,
        })
