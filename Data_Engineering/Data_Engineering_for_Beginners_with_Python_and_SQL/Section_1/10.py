# Creating a list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", True, 3.14]
 
# Printing the lists
print(fruits)       # Output: ['apple', 'banana', 'orange']
print(numbers)      # Output: [1, 2, 3, 4, 5]
print(mixed_list)   # Output: [1, 'apple', True, 3.14]

fruits = ["apple", "banana", "orange"]
print(fruits[0])     # Output: apple
print(fruits[1])     # Output: banana
print(fruits[2])     # Output: orange

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # Output: [2, 3, 4]
print(numbers[:3])    # Output: [1, 2, 3]
print(numbers[2:])    # Output: [3, 4, 5]

fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)         # Output: ['apple', 'grape', 'orange']

fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)         # Output: ['apple', 'banana', 'orange', 'grape']

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10)
print(numbers)        # Output: [1, 2, 10, 3, 4, 5]

fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")
print(fruits)         # Output: ['apple', 'orange', 'banana']

numbers = [1, 2, 3, 4, 5]
popped = numbers.pop(3)
print(numbers)        # Output: [1, 2, 3, 5]
print(popped)         # Output: 4

fruits = ["apple", "banana", "orange"]
del fruits[1]
print(fruits)         # Output: ['apple', 'orange']

# Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers if num % 2 == 0]
print(squared)        # Output: [4, 16]
 
# Example: Create a list of even numbers from 1 to 10
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)          # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
minimum = min(numbers)
maximum = max(numbers)
print(minimum)        # Output: 1
print(maximum)        # Output: 5