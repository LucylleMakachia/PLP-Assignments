# Base class
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def use_power(self):
        print(f"{self.name} uses their superpower: {self.power}!")

    def reveal_weakness(self):
        print(f"{self.name}'s weakness is {self.weakness}.")

# Derived class (Inheritance)
class Sidekick(Superhero):
    def __init__(self, name, power, weakness, hero):
        super().__init__(name, power, weakness)
        self.hero = hero

    def assist(self):
        print(f"{self.name} assists their hero, {self.hero}!")

# Create objects
hero = Superhero("Captain Code", "Debugging at lightning speed", "Syntax errors")
sidekick = Sidekick("Bug Buster", "Squashing bugs", "Infinite loops", "Captain Code")

# Use methods
hero.use_power()
hero.reveal_weakness()
sidekick.use_power()
sidekick.assist()
