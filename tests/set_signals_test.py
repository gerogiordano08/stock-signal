import unittest
from unittest.mock import patch
from src.set_signals import register_stockname, get_time

class TestRegisterStockname(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["aapl", 'Y'])
    def test_yn_y_returns_stockname(self, patch_input):
        result = register_stockname()
        self.assertEqual(result, "AAPL")
        
    @patch('builtins.input', side_effect=["aapl", 'n'])
    def test_yn_n_returns_empty_string(self, patch_input):
        result = register_stockname()
        self.assertEqual(result, "")
        
    @patch('builtins.input', side_effect=["aapl", 'w'])
    def test_yn_not_valid_returns_empty_string(self, patch_input):
        result = register_stockname()
        self.assertEqual(result, "")

    @patch('builtins.input', side_effect=["aapl", '7'])
    def test_yn_number_returns_empty_string(self, patch_input):
        result = register_stockname()
        self.assertEqual(result, "")
        
class TestGetTime(unittest.TestCase):
    @patch('builtins.input', side_effect=["9", 'Y'])
    def test_yn_y_returns_time(self, patch_input):
        result = get_time()
        self.assertEqual(result, 9)
        
    @patch('builtins.input', side_effect=["aapl", 'Y'])
    def test_yn_str_returns_0(self, patch_input):
        result = get_time()
        self.assertEqual(result, 0)
        
    @patch('builtins.input', side_effect=["9", 'n'])
    def test_yn_n_returns_0(self, patch_input):
        result = get_time()
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=["9", '7'])
    def test_yn_invalid_returns_empty_string(self, patch_input):
        result = get_time()
        self.assertEqual(result, 0)