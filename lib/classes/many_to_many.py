class NationalPark:

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string equal to or greater than 3 characters")

    @property
    def name(self):
        return self._name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        trips = self.trips()
        visit_counts = {}
        most_freq_visitor = None
        max_visits = 0

        for trip in trips:
            visitor = trip.visitor
            if visitor in visit_counts:
                visit_counts[visitor] += 1
            else:
                visit_counts[visitor] = 1
        
        for visitor, count in visit_counts.items():
            if count > max_visits:
                most_freq_visitor = visitor
                max_visits = count
        return most_freq_visitor if most_freq_visitor else None


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise ValueError("Start date must be a string and be equal to or longer than 7 characters")

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise ValueError(" End date must be a string and be equal to or longer than 7 characters")
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise ValueError("Visitor must be an instance of the Visitor class")
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise ValueError("National park must be an instance of the NationalPark class")

class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        return sum(1 for trip in Trip.all if trip.visitor == self and trip.national_park == park)
        