from datetime import date


class DatePeriodUtil:
    @staticmethod
    def are_overlapping(period1, period2):
        return ((period1.get_start() <= period2.get_start()) and (
                DatePeriodUtil.is_in_period(period1.get_end(), period2) or period1.get_end() > period2.get_end())) or \
               ((DatePeriodUtil.is_in_period(period1.get_start(),
                                             period2) or period1.get_start() < period2.get_start()) and (
                        period1.get_end() >= period2.get_end()))

    @staticmethod
    def is_in_period(date_val, period):
        return (period.get_start() < date_val < period.get_end()) or (date_val == period.get_start()) or (
                date_val == period.get_end())
