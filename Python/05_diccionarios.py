daniel = {
    'name': 'Daniel',
    'last_name': 'Freire',
    'age': 26,
    'salary': 1.01,
    'children': [],
    'married': False,
    'lottery': None,
    'pet': {
        'name': 'Toby',
        'age': 3
    }
}

print(daniel)
print(daniel['name'])  # Daniel
print(daniel['pet']['name'])  # Toby
print(daniel.get('lastName'))
daniel.pop('married')
print(daniel)
print(daniel.values())
for value in daniel.values():
    print(f'Value: {value}')

for key in daniel.keys():
    print(f'Key: {key}, value: {daniel[key]}')

for key, value in daniel.items():
    print(f'Key: {key}, value: {daniel[key]}')

daniel['profession'] = 'teacher'
new_values = {'weight': 0, 'height': 1}
daniel.update(new_values)
print(daniel)



