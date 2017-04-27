TYPE_NEW_RELEASE="New Release"
TYPE_REGULAR = "Regular"
TYPE_CHILDREN = "Children"
TYPE_UNKNOWN = "Unknown"
MOVIE_TYPES = set([TYPE_NEW_RELEASE, TYPE_REGULAR, TYPE_CHILDREN, TYPE_UNKNOWN])

class Movie(object):
    def __init__(self, name, movietype=TYPE_UNKNOWN):
        self.name = name
        if movietype not in MOVIE_TYPES:
            raise TypeError("invalid movie type")
        self.price = self.price_code(movietype)

    def price_code(self, price_type):
        if price_type is TYPE_CHILDREN:
            return ChildrensPrice()
        elif price_type is TYPE_NEW_RELEASE:
            return NewReleasePrice()
        elif price_type is TYPE_REGULAR:
            return RegularPrice()
        else:
            raise TypeError("invalid movie type")

    def get_charge(self, days_rented):
        return self.price.get_charge(days_rented)

    def get_points(self, days_rented):
        return self.price.get_points(days_rented)

class Price(object):
    def __init__(self):
        self.min_days = 1
        self.daily_rate = 1.5

    def get_charge(self, days_rented):
        if days_rented <= self.min_days:
            return self.daily_rate
        else:
            return self.daily_rate * (1 + days_rented - self.min_days)

    def get_points(self, days_rented=1):
        return 1

class ChildrensPrice(Price):
    def __init__(self):
        super(ChildrensPrice, self).__init__()
        self.min_days = 3

class RegularPrice(Price):
    def __init__(self):
        super(RegularPrice, self).__init__()
        self.min_days = 2

class NewReleasePrice(Price):
    def __init__(self):
        super(NewReleasePrice, self).__init__()
        self.daily_rate = 3

    def get_points(self, days_rented):
        return 2 if days_rented > 1 else 1


