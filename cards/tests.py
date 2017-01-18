from django.test import TestCase

from .models import Card


class CardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(text='foo bar')
        Card.objects.create(text='bar foo', secondary_text='bar foo 2')
        Card.objects.create()

    def test_card_creation(self):
        card = Card.objects.get(pk=1)
        cards = Card.objects.all()
        print cards
        self.assertEqual(card.text, 'foo bar')
