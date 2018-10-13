numberArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numberArray:
    print(number)

for index in range(0, 5):
    print(f'Number of iteration: {index}')

for index in range(3):
    print(f'Number of iteration: {index}')

for index in range(7, 10):
    print(f'Number of iteration: {index}')

for index in range(10):
    print(f'Number of iteration: {index}')
    if index == 6:
        break  # Stops the loop execution

for index in range(10):
    if index == 6:
        continue  # Stops the execution of the current iteration
    print(f'Number of iteration: {index}')

auxNumber = 0
while auxNumber < 10:
    print(f'Aux number: {auxNumber}')
    auxNumber += 1

auxNumber2 = 0
while True:
    print(f'Aux number: {auxNumber2}')
    auxNumber2 += 1
    if auxNumber2 == 5:
        break



