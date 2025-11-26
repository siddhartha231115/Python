class bmw:
    def start(self):
        print("bmw: starting engine with smooth ignition.")
    def stop(self):
        print("bmw: stopping engine with soft shutdown.")
class ferrari:
    def start(self):
        print("ferrari: engine roars to life aggressively!")
    def stop(self):
        print("ferrari: engine powers down with a sporty rumble.")
def car_actions(car):
    car.start()
    car.stop()
bmw_car = bmw()
ferrari_car = ferrari()
car_list = [bmw_car, ferrari_car]
for car in car_list:
    car_actions(car)