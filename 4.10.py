numbers = [value**3 for value in range(1,13)]
print("The first three items in the list are:")
numbers_3 = numbers[:3]
print(numbers_3)

print("\nThree items from the middle of the list are:")
numbers_middle = numbers[4:7]
print(numbers_middle)

print("\nThe last three items in the list are:")
numbers_last = numbers[-3:]
print(numbers_last)