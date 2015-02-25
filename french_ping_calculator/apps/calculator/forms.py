from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms_foundation import layout as _l


COEF = ((0.5, 0.5), (0.75, 0.75), (1, 1), (1.25, 1.25), (1.5, 1.5))
OUTCOMES = (('victory', _('Victory')), ('defeat', _('Defeat')))


class PlayerForm(forms.Form):
    player_point = forms.IntegerField(label=_('Player ranking'))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = ''
        self.helper.layout = _l.Layout(
            _l.Fieldset(
                _('Your points'),
                _l.Row(
                    _l.Column(
                        'player_point',
                        css_class='large-5'
                    ),
                    css_class='large-9'
                )
            ),
        )
        super(PlayerForm, self).__init__(*args, **kwargs)


class MatchForm(forms.Form):
    opponent_point = forms.IntegerField(label=_('Opponent ranking'))
    coef = forms.ChoiceField(choices=COEF)
    is_won = forms.ChoiceField(
        label=_("Did you win the match?"),
        choices=(('yes', _("Yes")), ('no', _("No"))),
        required=True,
	widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = ''
        self.helper.layout = _l.Layout(
            _l.Row(
                _l.Column(
                    _('opponent_point'),
                    css_class='large-5'
                ),
                _l.Column(
                    _('coef'),
                    css_class='large-2'
                ),
                _l.Column(
                    _('is_won'),
                    css_class='large-4 end radio_field',
                ),
                _l.Button(
                    'remove-form',
                    _('X'),
                    css_class='tiny large-1 alert remove-form disabled'
                ),
                css_class='large-9 match',
            )
        )

        super(MatchForm, self).__init__(*args, **kwargs)
