class SUV:
    def __init__(self):
        self.type = "SUV"

    def four_wheel(self):
        print("4 Wheels Drive")

    def suv_specific_action(self):
        print("SUV specific action")

class Sedan:
    def __init__(self):
        self.type = "Sedan"

    def two_wheel_drive(self):
        print("2 Wheels Drive")

    def sedan_sepecific_action(self):
        print("Sedan specific aciton")


def main():
    cars = [SUV(), Sedan()]

    for car in cars:
        car_type = car.type
        if car_type == "SUV":
            car.four_wheel()
            car.suv_specific_action()
        elif car_type == "Sedan":
            car.two_wheel_drive()
            car.sedan_sepecific_action()
        else:
            pass

main()