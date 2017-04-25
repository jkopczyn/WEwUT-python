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
