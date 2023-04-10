from datetime import date


class DatePeriodUtil:
    @staticmethod
    def are_overlapping(period1, period2):
        # We only need to check if the start of one period is within the other period. You don't need to check ends at all.
        # After all, if the end of B is within A, then either the start of B is also in A, or the start of A is in B. So why even
        # bother checking the ends? It's wasted operations
        return DatePeriodUtil.is_in_period(period1.get_start(), period2) or DatePeriodUtil.is_in_period(period2.get_start(), period1)

    @staticmethod
    def is_in_period(date_val, period):
        return (period.get_start() < date_val < period.get_end()) or (date_val == period.get_start()) or (
                date_val == period.get_end())
