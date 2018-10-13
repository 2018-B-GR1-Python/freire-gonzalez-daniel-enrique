tuple = (1, 2, 3, 2, 3, 3, 'a', 'b', 'c', 'c')
print(tuple)

for number in tuple:
    print(f'Number: {number}')

print(tuple.index(1))  # To get the index of a value
print(tuple.count(2))  # To count the occurrences of a value
print(tuple[-1])
print(tuple[:2])

print(set(tuple))  # Tuple without repetitions

for t in set(tuple):
    print(f'Value: {t}')



