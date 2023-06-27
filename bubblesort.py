Implement a program to sort a list of numbers in ascending order using the Bubble Sort algorithm:
python
Copy code
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

input_list = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_list.split()]

bubble_sort(numbers)

print("Sorted numbers in ascending order:")
for num in numbers:
    print(num)
