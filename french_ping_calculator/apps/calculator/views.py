from django.shortcuts import render
from django.forms.formsets import formset_factory
from django.views.generic import View

from calculator.forms import MatchForm
from calculator.forms import PlayerForm
from calculator.utils import Match
from calculator.utils import Competition


class PingCalculatorView(View):

    def __init__(self, **kwargs):
        super(PingCalculatorView, self).__init__(**kwargs)
        self.match_formset = formset_factory(MatchForm, max_num=5)
        self.player_form = PlayerForm(prefix='player')
        
    def get(self, request, *args, **kwargs):
        return render(request, 'ping_calculator.html', {
            'match_formset': self.match_formset(prefix='match'),
            'player_form': self.player_form,
        })

    def post(self, request, *args, **kwargs):
        self.match_formset = self.match_formset(request.POST, request.FILES, prefix='match')
        self.player_form = PlayerForm(request.POST, request.FILES, prefix='player')
        if self.match_formset.is_valid() and self.player_form.is_valid():
            competition = Competition()
            for form in self.match_formset.cleaned_data:
                player_point = self.player_form.cleaned_data.get('player_point')
                match = Match(player_point=player_point, **form)
                competition.matchs.append(match)
            return render(request, 'ping_calculator.html', {
                'match_formset': self.match_formset,
                'player_form': self.player_form,
                "competition": competition
            })
        else:
            return render(request, 'ping_calculator.html', {
                'match_formset': self.match_formset,
                'player_form': self.player_form,
            })