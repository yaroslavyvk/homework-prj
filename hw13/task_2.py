class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        complate_name = f"{self.name} {other_country.name}"
        total_population = self.population + other_country.population
        return Country(complate_name, total_population)

    def __str__(self):
        return f"{self.name} - Population: {self.population}"


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina)
