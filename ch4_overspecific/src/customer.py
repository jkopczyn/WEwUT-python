class Customer(object):
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_rentals(self):
        return self.rentals

    def recent_rentals(self):
        prefix = "Recent rentals:"
        return (prefix + "\n".join([""]+[r.get_movie(
            True
            ).get_title(
                "{0} starring {1} {2}", 2
                ) for r in self.rentals[:3]]))


    def get_total_charge(self):
        return sum(r.get_charge() for r in self.rentals)

    def get_total_points(self):
        return sum(r.get_points() for r in self.rentals)
