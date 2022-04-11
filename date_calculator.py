import datetime


class DateCalculator:
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self):
        self._day = 0
        self._month = 0
        self._year = 0

    def _set_date(self, date: datetime.datetime):
        self._day = date.day
        self._month = date.month
        self._year = date.year

    def _get_days_in_month(self) -> int:
        if self._month == 2:
            return self._calculate_days_feb()
        return self.days_in_month[self._month - 1]

    def _calculate_days_feb(self) -> int:
        if self._year % 4 == 0:
            return self.days_in_month[1] + 1
        return self.days_in_month[1]

    def _next_day(self):
        if self._day == self._get_days_in_month():
            self._day = 1
            if self._month == 12:
                self._month = 1
                self._year += 1
            else:
                self._month += 1
        else:
            self._day += 1

    def add_to_date(self, date: datetime.datetime, days: int) -> datetime.datetime:
        self._set_date(date)
        for i in range(days):
            self._next_day()
        return datetime.datetime(self._year, self._month, self._day)


if __name__ == '__main__':
    calculator = DateCalculator()
    days_to_add = 1024
    date = datetime.datetime(year=2004, month=2, day=10)
    new_date = calculator.add_to_date(date, days_to_add)
    print(new_date)
    print(date + datetime.timedelta(days=days_to_add))
    assert new_date == date + datetime.timedelta(days=days_to_add)
