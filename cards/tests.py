from django.test import TestCase

from .models import Card


class CardTestCase(TestCase):

    def setUp(self):
        Card.objects.create(title='card 01', text='foo bar')
        Card.objects.create(title='card 02', text='bar foo', secondary_text='bar foo 2')

    def test_card_creation(self):
        card = Card.objects.get(pk=1)
        second_card = Card.objects.get(pk=2)
        self.assertEqual(card.text, 'foo bar')
        self.assertEqual(second_card.secondary_text, 'bar foo 2')
