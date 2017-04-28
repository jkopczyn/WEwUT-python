class Store(object):
    def __init__(self, movies):
        self.stock = {}
        for m in movies:
            if m in self.stock:
                self.stock[m] += 1
            else:
                self.stock[m] = 1

    def get_availability(self, movie):
        return (movie in self.stock and self.stock[movie] > 0)

    def check_out(self, movie):
        if movie not in self.stock:
            raise ValueError("Movie not stocked in this store")
        elif self.stock[movie] > 0:
            self.stock[movie] -= 1
            return True
        else:
            return False
