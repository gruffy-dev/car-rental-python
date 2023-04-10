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
       
    #Putting variables here is obv bad but it's for showcasing this (now fixed) bug.
    periodA = DatePeriod(date(2000,5,23),date(2000,6,23))
    periodB = DatePeriod(date(2000,5,24),date(2000,6,22))
    #Period A sits wholly in B.

    #This test tries is period A is within period B, which should be an overlap.
    def test_overlap_A_in_B(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.periodA, self.periodB))
        #This pairing should be an overlap, as A sits wholly within B.
    
    #This test tries is period B is within period A, which should be an overlap.
    def test_overlap_B_in_A(self):
        self.assertTrue(DatePeriodUtil.are_overlapping(self.periodB, self.periodA))
        #This pairing should be an overlap, as B sits wholly within A.


if __name__ == '__main__':
    unittest.main()
