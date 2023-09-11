class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other_country):
        combinate_name = f'{self.name} {other_country.name}'
        combinate_population = self.population + other_country.population
        return Country(combinate_name, combinate_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.name, bosnia_herzegovina.population)
