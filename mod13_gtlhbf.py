import unittest
from datetime import datetime

class TestStockInputs(unittest.TestCase):
    take_input = False

    # symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        symbol = 'AAPL' if not self.take_input else input("Enter a stock symbol: ")

        # has to be alphabetic
        self.assertTrue(symbol.isalpha())
        # has to be capitalized
        self.assertEqual(symbol, symbol.upper())
        # has to be 1-7 characters
        self.assertTrue(1 <= len(symbol) <= 7)

    # chart type: 1 numeric character, 1 or 2
    def test_chart_type(self):
        chart_type = "1" if not self.take_input else input("Enter a chart type (1 or 2): ")

        # has to be numeric
        self.assertTrue(chart_type.isnumeric())
        # has to be 1 or 2
        self.assertIn(int(chart_type), [1, 2])
        
    # time series: 1 numeric character, 1 - 4
    def test_time_series(self):
        time_series = "1" if not self.take_input else input("Enter a time series (1 - 4): ")

        # has to be numeric
        self.assertTrue(time_series.isnumeric())
        # has to be 1 - 4
        self.assertIn(int(time_series), [1, 2, 3, 4])

    # start date: YYYY-MM-DD
    def test_start_date(self):
        start_date = '2023-01-01' if not self.take_input else input("Enter a start date (YYYY-MM-DD): ")

        # has to be a valid date
        self.assertTrue(datetime.strptime(start_date, '%Y-%m-%d'))

    # end date: YYYY-MM-DD
    def test_end_date(self):
        end_date = '2023-01-01' if not self.take_input else input("Enter an end date (YYYY-MM-DD): ")

        # has to be a valid date
        self.assertTrue(datetime.strptime(end_date, '%Y-%m-%d'))

if __name__ == '__main__':
    unittest.main()