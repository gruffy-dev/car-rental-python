from datetime import date
from main.utils.DatePeriodUtil import DatePeriodUtil
from main.utils.DatePeriod import DatePeriod
import unittest


class DatePeriodUtilTest(unittest.TestCase):
    BASE_PERIOD = DatePeriod(date(2023, 1, 14), date(2023, 2, 5))

    START_OVERLAP = DatePeriod(date(2023, 1, 12), date(2023, 1, 16))
    WHOLLY_IN_PERIOD = DatePeriod(date(2023, 1, 15), date(2023, 2, 4))
    END_OVERLAP = DatePeriod(date(2023, 2, 4), date(2023, 2, 6))

    SINGLE_DATE_PERIOD_START = DatePeriod(date(2023, 1, 14), date(2023, 1, 14))
    SINGLE_DATE_PERIOD_END = DatePeriod(date(2023, 2, 5), date(2023, 2, 5))

    OVERLAPPING_START_DAY = DatePeriod(date(2023, 1, 13), date(2023, 1, 14))
    OVERLAPPING_END_DAY = DatePeriod(date(2023, 2, 5), date(2023, 2, 6))

    PERIOD_BEFORE = DatePeriod(date(2023, 1, 1), date(2023, 1, 13))
    PERIOD_AFTER = DatePeriod(date(2023, 2, 6), date(2023, 2, 12))

    def test_for_overlapping_periods_with_start_overlap(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.START_OVERLAP))

    def test_for_overlapping_periods_with_end_overlap(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.END_OVERLAP))

    def test_for_overlapping_periods_with_whole_period_overlap(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.WHOLLY_IN_PERIOD))

    def test_for_overlapping_periods_with_single_date_period_with_start_overlap(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.SINGLE_DATE_PERIOD_START))

    def test_for_overlapping_periods_with_single_date_period_with_end_overlap(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.SINGLE_DATE_PERIOD_END))

    def test_for_overlapping_periods_with_start_date_specifically_overlapping(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.OVERLAPPING_START_DAY))

    def test_for_overlapping_periods_with_end_date_specifically_overlapping(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.OVERLAPPING_END_DAY))

    def test_for_non_overlapping_period_before(self):
        self.assertFalse(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.PERIOD_BEFORE))

    def test_for_non_overlapping_period_after(self):
        self.assertFalse(DatePeriodUtil.are_overlapping(self.BASE_PERIOD, self.PERIOD_AFTER))


if __name__ == '__main__':
    unittest.main()
