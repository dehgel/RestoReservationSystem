class ReservationData:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = int(adults)
        self.children = int(children)

    # Calculation of subtotal
    def subtotal(self):
        return self.adults * 500 + self.children * 300