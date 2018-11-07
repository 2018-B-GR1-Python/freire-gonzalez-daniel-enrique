class CarOne:
    pass  # class not defined yet


class School:

    # category_value = 4
    __city = 'Quito'  # private attribute
    country = 'Ecuador'  # public attribute

    def __init__(self, name, category_value=4):  # constructor
        print(self)
        print('Hi constructor')
        self.name = name
        self.category_value = category_value

    def greet(self):
        print(f'Hi from {self.name} placed in {self.__city} - {self.country}')

    def category(self):
        return self.__compute_category()

    def __compute_category(self):  # private function
        return self.category_value * 3

    def __str__(self):
        return 'School'


school = School('School')
school.category_value = 2
print(school)
school.greet()
print(school.category())


class Car:
    _assembled = 'Quito'  # protected attribute
    sits_number = 5

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __init__(self, name, color, another_color=''):
        self.name = name
        self.color = color
        self.another_color = another_color

    def change_assembly(self, assembled):
        self._assembled = assembled

    def __max_number_passengers(self):
        return self.sits_number + 3

    def __str__(self):
        return (f'{self.name}\n'
                f'{self.color}\n'
                f'{self.another_color}\n'
                f'{self.sits_number}\n'
                f'{self._assembled}\n'
                f'{self.__max_number_passengers()}\n')


bmw = Car('BMW', 'White')
print(bmw)


class BMW(Car):
    def __init__(self, color, name, another_color):
        super().__init__(name, color, another_color)
        print('constructor')
        print(self._assembled)


my_car = BMW('Black', 'X6', 'Brown')
print(my_car)
