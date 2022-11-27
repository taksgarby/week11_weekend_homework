import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spade", 1)
        self.card1 = Card("Spade", 2)
        self.card2 = Card("Spade", 3)

    def test_check_for_ace__is_not_ace(self):
 
        # act
        result = CardGame.check_for_ace(self, self.card1)

        # assert
        self.assertEqual(False, result)


    def test_check_for_ace__is_ace(self):
     
        # act
        result = CardGame.check_for_ace(self, self.card)

        # assert
        self.assertEqual(True, result)


    def test_highest_value_card_is_returned(self):

        result = CardGame.highest_card(self, self.card1, self.card2)
        
        self.assertEqual(self.card2, result)
    

    def test_cards_total_value(self):

        # arrange
        cards = [self.card, self.card1, self.card2]
        
        # act
        result = CardGame.cards_total(self, cards)
        
        # assert   
        self.assertEqual("You have a total of 6", result)