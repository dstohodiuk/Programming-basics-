class Denys:
    name = None
    last_name = None
    birth_year = None

    def calculates_the_course(birth_year: int):
        my_year = 2007
        rate = 1.0 + (birth_year - my_year) * 0.05
        return max(rate, 0.1)

    print(f"Your course: {calculates_the_course(2003):.2}")

    def get(self, name, last_name):
        self.name = 'Denys'
        self.last_name = 'Stohodiuk'
        result = [self.name, self.last_name]

    print(result)
