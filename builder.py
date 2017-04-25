class CustomerBuilder(object):
    def __init__(self, name="Jim", rentals=None, builders=None):
        self.name = name
        if rentals:
            self.rentals = rentals
        elif builders:
            self.rentals = [builder.build() for builder in builders]
        else:
            self.rentals = []

    def build(self):
        result = Customer(self.name)
        for rental in self.rentals:
            result.add_rental(rental)
        return result

class Customer(object):
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_rentals(self):
        return self.rentals

    def statement(self):
        result = "Rental record for {0}\n".format(self.name)
        result += "\n".join("\t {0}".format(r.get_line_item()) for
                r in self.rentals)
        result += ("\nAmount owed is {0}\n" +
        "You earned {1} frequent renter points").format(
                self.get_total_charge(),
                self.get_total_points())
        return result

    def html_statement(self):
        result = "<h1>Rental record for </em>{1}</em></h1>\n".format(self.name)
        result += "\n".join("<p>{0}</p>".format(r.get_line_item()) for
                r in self.rentals)
        result += ("\n<p>Amount owed is <i>{0}</i></p>\n" +
        "<p>You earned <i>{1} frequent renter points</i></p>").format(
                self.get_total_charge(),
                self.get_total_points())
        return result

    def get_total_charge(self):
        return sum(r.get_charge() for r in self.rentals)

    def get_total_points(self):
        return sum(r.get_points() for r in self.rentals)

a = CustomerBuilder()
b = a.build()

class RentalBuilder(object):
    def __init__(self, movie=None, days=3, builder=None):
        self.movie = movie
        self.days = days
        if builder and not movie:
            self.movie = builder.build()

    def build(self):
        return Rental(self.movie, self.days)

class Rental(object):
    def __init__(self, movie, days):
        self.movie = movie
        self.days = days

    def get_charge(self):
        self.movie.get_charge(self.days)

    def get_points(self):
        self.movie.get_points(self.days)

    def get_line_item(self):
        return "{0} {1}".format(self.movie.title, self.get_charge())


c = RentalBuilder()
d = c.build()

TYPE_NEW_RELEASE="New Release"
TYPES = set([TYPE_NEW_RELEASE])

class MovieBuilder(object):
    def __init__(self, name="Godfather 4", movietype=TYPE_NEW_RELEASE):
        self.name = name
        if movietype not in TYPES:
            raise "Argument Error: invalid movie type"
        self.type = movietype

    def build(self):
        return Movie(self.name, self.type)
