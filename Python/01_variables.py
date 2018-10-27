print('Hello world')
age: int = 20
salary: float = 1.02
print(age + int(salary))

name: str = 'Daniel'  # Comment
last_name = "Freire"
apellido_materno = """González"""
print(name == last_name)  # True / False
print(last_name == apellido_materno)  # True / False
print(apellido_materno)
print(int(True))  # 1
print(int(False))  # 0
print(str(True))  # 'True'
print(str(False))  # 'False'

print('daniel freire'.capitalize())  # Daniel freire
nombre_completo = 'daniel freire'.split(' ')  # ['daniel', 'freire']
print(nombre_completo[0].capitalize() + ' ' + nombre_completo[1].capitalize())  # Daniel Freire
print('Daniel'.isalpha())  # True
print('Daniel10'.isalpha())  # False
print('10'.isnumeric())  # True
print('Daniel10'.isnumeric())  # False
print('10'.isalnum())  # True
print('Daniel10'.isalnum())  # True
print('My name is {0} {1}'.format(nombre_completo[0].capitalize(), 'Freire'))
print(f'My name is {nombre_completo[0].capitalize()} {nombre_completo[1].capitalize()}')
print(r'')  # raw
null = None  # null
print(null)
