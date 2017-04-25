class Customer_Builder(object):
    def __init__(self, name="Jim", rentals=None, builders=None):
        self.name = name
        if rentals:
            self.rentals = rentals
        elif builders:
            self.rentals = [builder.build() for builder in builders]
        else:
            self.rentals = []

    def build_customer(self):
        result = Customer.new(self.name)
        for rental in self.rentals:
            result.add_rental(rental)
        return result

class Customer(object):
    def __init__(self, name):
        self.name = name

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_rentals(self):
        return self.rentals

    def statement(self):
        result = "Rental record for {1}\n".format(self.name)
        result += "\n".join("\t {1}".format(r.get_line_item()) for
                r in self.rentals)
        result += ("\nAmount owed is {1}\n" +
        "You earned {2} frequent renter points").format(
                self.get_total_charge(),
                self.get_total_points())
        return result

    def html_statement(self):
        result = "<h1>Rental record for </em>{1}</em></h1>\n".format(self.name)
        result += "\n".join("<p>{1}</p>".format(r.get_line_item()) for
                r in self.rentals)
        result += ("\n<p>Amount owed is <i>{1}</i></p>\n" +
        "<p>You earned <i>{2} frequent renter points</i></p>").format(
                self.get_total_charge(),
                self.get_total_points())
        return result

    def get_total_charge(self):
        return sum(r.get_charge() for r in self.rentals)

    def get_total_points(self):
        return sum(r.get_points() for r in self.rentals)
