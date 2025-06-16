from datetime import date

class Calendar:
    @property
    def today(self):
        return date.today()


class CalendarStub:
    def __init__(self, start_date):
        self._today = start_date

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self, new_date):
        self._today = new_date
