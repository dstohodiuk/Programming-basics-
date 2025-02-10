class Denys:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculates_the_course(birth_year: int):
        my_year = 2007
        rate = 1.0 + (birth_year - my_year) * 0.05
        return max(rate, 0.1)

    print(f"Your course: {calculates_the_course(2003):.2}")

    def set_name(self):
        return [self.name, self.last_name]


name_last_name = Denys('Denys', 'Stohodiuk',)
list_name = name_last_name.set_name()
print(list_name)
