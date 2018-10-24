class Car:
    pass  # class not defined yet


bm = Car()
print(bm)


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
