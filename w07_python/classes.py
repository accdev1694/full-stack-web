class Point:
    # below is a magic method that gets called everytime i try to create a new object from this class
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2,10)
print(p.x, p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False         
        self.passengers.append(name)
        return True

    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(5)
people = ["Oloche", "Gold", "Emma", "Almond", "Comfort", "James"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"{person} has been addedd successfully")
    else:
        print(f"There is no available seats for {person}")