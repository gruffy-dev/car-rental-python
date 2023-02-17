import unittest
from datetime import date
from main.utils.DatePeriod import DatePeriod


class DatePeriodTest(unittest.TestCase):

    def test_valid_date_period_construction(self):
        DatePeriod(date(2023, 1, 15), date(2023, 1, 16))

    def test_valid_date_period_construction_start_end_same(self):
        DatePeriod(date(2023, 1, 15), date(2023, 1, 15))

    def test_invalid_date_period_construction(self):
        self.assertRaises(AssertionError, DatePeriod, date(2023, 1, 16), date(2023, 1, 15))
