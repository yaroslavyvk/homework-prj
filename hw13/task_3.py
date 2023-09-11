class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelarate(self):
        self.speed += 5 

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        return f"The {self.year} {self.brand} {self.model} is currently going {self.speed} kmh."


car1 = Car("Opel", "Astra", 1996, 80)
car1.accelarate()
car1.display_speed()
