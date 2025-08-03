# python -m unittest tests.test_trading_bot

from bot.trading_bot import TradingBot
import unittest

class Test_TradingBot(unittest.TestCase):
    def setUp(self):
        self.tb = TradingBot()

    def test_values_insert(self):
        self.tb.buy("AAPL", 2)
        self.tb.buy("BTC", 5)
        self.assertEqual(self.tb.portfolio["AAPL"], 2)
        self.assertEqual(self.tb.portfolio["BTC"], 5)

    def test_values_exist(self):
        """Example test that should fail."""
        self.tb.buy("AAPL", 2)
        self.assertEqual(self.tb.portfolio["AAPL"], 2)
        self.assertRaises(KeyError, lambda: self.tb.portfolio["NON_EXISTANT"])
    
    def test_values_delete(self):
        self.tb.buy("AAPL", 2)
        self.tb.buy("BTC", 5)
        self.assertEqual(self.tb.portfolio["AAPL"], 2)
        self.assertEqual(self.tb.portfolio["BTC"], 5)
        self.assertRaises(ValueError, lambda: self.tb.sell("AAPL", 5))
        self.tb.sell("AAPL", 1)
        self.assertEqual(self.tb.portfolio["AAPL"], 1)
    
    def test_values_add(self):
        self.tb.buy("AAPL", 2)
        self.assertEqual(self.tb.portfolio["AAPL"], 2)
        self.tb.buy("AAPL", 1)
        self.assertEqual(self.tb.portfolio["AAPL"], 3)
    
    def test_show_data(self):
        self.tb.buy("AAPL", 2)
        self.tb.buy("BTC", 5)
        self.assertEqual(self.tb.data, ['AAPL: 2', 'BTC: 5'])

if __name__ == '__main__':
    unittest.main()
