class Visitor:
    def __init__(self, name):
        self.name = name
        self._trips = []

    def add_trip(self, trip):
        self._trips.append(trip)

    def trips(self):
        return self._trips


class NationalPark:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 3:
            raise ValueError("Name must be a string longer than 3 characters")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name")

    def add_trip(self, trip):
        self._trips.append(trip)

    def trips(self):
        return self._trips

    def visitors(self):
        return list({trip.visitor for trip in self._trips})

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        visitor_count = {}
        for trip in self._trips:
            if trip.visitor not in visitor_count:
                visitor_count[trip.visitor] = 0
            visitor_count[trip.visitor] += 1
        return max(visitor_count, key=visitor_count.get)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(start_date, str) or len(start_date) != 8:
            raise ValueError("start_date must be a string of length 8")
        if not isinstance(end_date, str) or len(end_date) != 8:
            raise ValueError("end_date must be a string of length 8")

        self._start_date = start_date
        self._end_date = end_date
        self.visitor = visitor
        self.national_park = national_park
        Trip.all.append(self)
        national_park.add_trip(self)
        visitor.add_trip(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) == 8:
            self._start_date = value
        else:
            raise ValueError("start_date must be a string of length 8")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) == 8:
            self._end_date = value
        else:
            raise ValueError("end_date must be a string of length 8")
