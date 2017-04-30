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

    def get_title(self):
        return self.name

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
        self.min_price = self.daily_rate

    def get_charge(self, days_rented):
        if days_rented <= self.min_days:
            return self.min_price
        else:
            return self.min_price+(days_rented - self.min_days)*self.daily_rate

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
        self.min_price = 2.0

class NewReleasePrice(Price):
    def __init__(self):
        super(NewReleasePrice, self).__init__()
        self.daily_rate = 3.0
        self.min_days = 0
        self.min_price = 0

    def get_points(self, days_rented):
        return 2 if days_rented > 1 else 1


