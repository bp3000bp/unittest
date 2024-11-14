import unittest
import datetime

def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    return chart_type in {'1', '2'}

def validate_time_series(time_series):
    return time_series in {'1', '2', '3', '4'}

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):
    def test_symbol_valid(self):
        self.assertTrue(validate_symbol('AAPL'))

    def test_symbol_invalid_length(self):
        self.assertFalse(validate_symbol('APPLEINC'))

    def test_symbol_lower_case(self):
        self.assertFalse(validate_symbol('aapl'))

    def test_chart_type_valid(self):
        self.assertTrue(validate_chart_type('1'))

    def test_chart_type_invalid(self):
        self.assertFalse(validate_chart_type('3'))

    def test_time_series_valid(self):
        self.assertTrue(validate_time_series('4'))

    def test_time_series_invalid(self):
        self.assertFalse(validate_time_series('5'))

    def test_start_date_valid(self):
        self.assertTrue(validate_date('2022-01-01'))

    def test_start_date_invalid_format(self):
        self.assertFalse(validate_date('01-01-2022'))

    def test_end_date_valid(self):
        self.assertTrue(validate_date('2024-12-31'))

    def test_end_date_invalid(self):
        self.assertFalse(validate_date('2024-31-12'))

if __name__ == '__main__':
    unittest.main()
