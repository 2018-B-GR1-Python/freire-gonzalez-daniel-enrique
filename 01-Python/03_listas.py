array = []
numberArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
whateverArray = ['a', 1, True, False, None, 10.1, [1, 2, 3]]
print(numberArray[0:5])
print(numberArray[3:5])
print(numberArray[:5])
print(numberArray[2:])
print(numberArray[:])
print(numberArray[-1])
print(numberArray[-2])
print(numberArray[3:-2])
print(numberArray[-5:-2])
print(7 in numberArray)
print(15 in numberArray)
print(len(numberArray))
numberArray.append(10)
print(numberArray)
numberArray.pop(-3)
print(numberArray)
numberArray.insert(1, 1.2)
print(numberArray)
del numberArray[1]
print(numberArray)
del numberArray[1:4]
print(numberArray)



