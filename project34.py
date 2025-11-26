class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
    def fare(self):
        base_fare = super().fare()
        extra_charge = base_fare * 0.10
        return base_fare + extra_charge
bus = Bus(50)
print("total bus fare:", bus.fare())