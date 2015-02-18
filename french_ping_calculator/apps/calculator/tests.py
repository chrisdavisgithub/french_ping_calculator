from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from calculator.forms import PlayerForm
from calculator.forms import MatchForm


class PingCalculatorTestCase(TestCase):
    """Calculation view test case"""

    def test_get(self):

        client = Client()
        response = client.get('')

        self.assertTrue(isinstance(response.context['player_form'], PlayerForm))
        for item in response.context['match_formset']:
            self.assertTrue(isinstance(item, MatchForm))

    def test_post(self):

        client = Client()
        response = client.post(
            '',
            {'player-player_point': 500,
             'match-TOTAL_FORMS': '1',
             'match-INITIAL_FORMS': '0',
             'match-MAX-NUM-FORMS': '',
             'match-0-opponent_point':500,
             'match-0-coef': 1,
             'match-0-is_won':'yes'},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['competition'].result, 6)
        
        

    