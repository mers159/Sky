class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passanger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passanger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

        # there's an error