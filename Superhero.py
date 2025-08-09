class Superhero:
    def _init_(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin 

        def introduce(self):
            return f"I am {self.name} from {self.origin}, and I weild the power of {self.power}!"

        def use_power(self):
            return f"{self.name} uses {self.power} to save the day!"
            
class FlyingHero(Suerhero):
    def _init_(self, name, power, origin, flight_speed):
        super()._init_(name, power, origin)
        self.flight_speed = flight_speed

        def use_power(self):
            return f" {self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!" 
