# Problem1: Implement a Python program that takes a list of integers and returns a new list containing only the even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]# Using list comprehension to filter even numbers
print(even_numbers)

#___________________________________________________________________________________________________________________________________#

# Problem2: Create a function that accepts a tuple of numbers and returns the sum of all the elements

def sum_tuple_elements(numbers_tuple):
    # Summing the elements of the tuple using a for loop
    total_sum = 0
    for num in numbers_tuple:
        total_sum += num
    return total_sum

# usage
numbers = (1, 2, 3, 4, 5)
total = sum_tuple_elements(numbers)
print(f"Sum of tuple: {total}")

#___________________________________________________________________________________________________________________________________#

# Problem3: Write a Python program to find the maximum and minimum values in a list without using built-in functions

numbers = [23, 45, 12, 67, 34, 89, 2, 56]

max_value = numbers[0]
min_value = numbers[0]

# Loop through the list starting from the second element
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Display results
print(max_value)
print(min_value)

#___________________________________________________________________________________________________________________________________#

# Problem4: Implement a function that removes all duplicates from a list while preserving the original order of elements

def remove_duplicates(list):
    sets = set()  
    result = []  

    for i in list:
        if i not in sets:
            result.append(i)  # Add item if not seen
            sets.add(i)       # Mark item 

    return result

# usage
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique_numbers = remove_duplicates(numbers)

print("The Original", numbers)
print("List without duplicates:", unique_numbers)

#___________________________________________________________________________________________________________________________________#

# Problem5: Create a dictionary that maps the first ten prime numbers to their squares

primes = [] # List to store the first 10 prime numbers
num = 2  # Start checking from 2

while len(primes) < 10:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1

prime_squares = {}  # Create a dictionary

for prime in primes:
    prime_squares[prime] = prime ** 2  # Manually map prime to its square
print(prime_squares)


#___________________________________________________________________________________________________________________________________#

# Problem6: Write a Python function that takes a string and counts the frequency of each character

def count_char_frequencies(str):
    frequency_dict = {}
    # Loop through each character in the string
    for char in str:
        if char in frequency_dict:
            frequency_dict[char] += 1  # Increment the count if character already exists
        else:
            frequency_dict[char] = 1   # Initialize the count for a new character
    
    return frequency_dict

# usage
input_string = "hello I am Nourhan Farghal"
char_frequencies = count_char_frequencies(input_string)
print(char_frequencies)

#___________________________________________________________________________________________________________________________________#

# Problem7: Implement a set operation that returns the intersection of two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = list(set(list1) & set(list2)) # Convert lists to sets and find the intersection
print( intersection)

#___________________________________________________________________________________________________________________________________#

# Problem8: Create a program that reverses the elements in a tuple

tup = (1, 2, 3, 4, 5)
reversed_tup = tup[::-1]# Reverse the tuple
print(f'The reverse of this tuple {tup} is {reversed_tup}')

#___________________________________________________________________________________________________________________________________#

# Problem9: Write a program that sorts a dictionary by its values.

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1])) # Sort the dictionary by its values
print(sorted_dict)


#___________________________________________________________________________________________________________________________________#

# Problem10: Implement a stack using a list. Include methods for pushing, popping, and checking if the stack is empty.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

# usage
stack = Stack()
stack.push(5)
stack.push(10)
print("Popped item:", stack.pop())
print("Is stack empty?", stack.is_empty())

#___________________________________________________________________________________________________________________________________#

# Problem11: Create a queue using collections.deque and implement enqueue and dequeue operations.

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

# usage
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print("Dequeued item:", queue.dequeue())
print("Is queue empty?", queue.is_empty())


#___________________________________________________________________________________________________________________________________#

# Problem12: Write a Python program that flattens a nested list into a single list.

nested = [1, [2, [3, 4], 5], 6]

stack = nested[:]
flat_list = []
while stack:
    item = stack.pop(0)  # Get the first element
    if isinstance(item, list):
        stack = item + stack  # Add list items to the stack at the front
    else:
        flat_list.append(item)

print(flat_list)


#___________________________________________________________________________________________________________________________________#

# Problem13: Implement a function that merges two dictionaries, adding values for keys that appear in both.

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)


#___________________________________________________________________________________________________________________________________#

# Problem14: Create a Python function that checks if a string is a palindrome using a deque.
from collections import deque

def is_palindrome(str):
    dequ = deque(str)
    while len(dequ) > 1:
        if dequ.popleft() != dequ.pop():
            return False
    return True

# usage
string = "racecar"
print(f"Is '{string}' a palindrome?", is_palindrome(string))

#___________________________________________________________________________________________________________________________________#

# Problem15: Implement a program that counts the occurrence of each word in a text file.
filename = "C:/Users/power/OneDrive - MAM (Faculty of Engineering)/Desktop/text file.txt"
word_count = {}

with open(filename, 'r') as file:
    for line in file:
        words = line.split()  # Split each line into words
        for word in words:
            word = word.lower()  # Convert to lowercase
            if word in word_count:
                word_count[word] += 1  # Increment the count
            else:
                word_count[word] = 1   # Initialize count for a new word

print(word_count)

#___________________________________________________________________________________________________________________________________#

# Problem16: Write a function that returns the nth Fibonacci number using recursion.
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

# usage
num = 10
print(f"The {num}th Fibonacci number is:", fibonacci(num))

#___________________________________________________________________________________________________________________________________#

# Problem17: Create a linked list class with methods to add elements at the beginning, end, and at a specific position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# usage
link = LinkedList()
link.add_to_beginning(1)
link.add_to_end(2)


#___________________________________________________________________________________________________________________________________#

# Problem18: Implement a binary search algorithm to find an element in a sorted list

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# usage
arr = [1, 2, 3, 4, 5, 6]
target = 4
print(f"Element {target} found at index:", binary_search(arr, target))

#___________________________________________________________________________________________________________________________________#

# Problem19: Write a Python program that finds the longest common prefix string among a list of strings.
strs = ["flower", "flow", "flight"]

if not strs:
    longest_prefix = ""
else:
    longest_prefix = strs[0]     # Start with the first string as a reference


    for string in strs[1:]:     # Compare the reference string with the others
        while not string.startswith(longest_prefix):
            longest_prefix = longest_prefix[:-1]  # Remove the last character
            if not longest_prefix:
                break
print(longest_prefix)



#___________________________________________________________________________________________________________________________________#

# Problem20: Implement a function that calculates the Levenshtein distance between two strings.
str1 = "kitten"
str2 = "sitting"

# Initialize a matrix of distances
m = len(str1) + 1
n = len(str2) + 1
dp = [[0] * n for _ in range(m)]

# Fill the base cases
for i in range(m):
    dp[i][0] = i
for j in range(n):
    dp[0][j] = j

# Fill the matrix
for i in range(1, m):
    for j in range(1, n):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
print(dp[-1][-1])

#___________________________________________________________________________________________________________________________________#

# Problem21: Write a program that finds all the unique pairs of numbers in a list that sum up to a specific target.
nums = [2, 4, 3, 5, 7, 8, 1]
target = 7

seen = set()
pairs = set()

for num in nums:
    complement = target - num
    if complement in seen:
        pairs.add((min(num, complement), max(num, complement)))
    seen.add(num)

print("Unique pairs that sum to", target, ":", pairs)

#___________________________________________________________________________________________________________________________________#

# Problem22: Create a program that generates all possible subsets of a given set.
s = [1, 2, 3]
subsets = [[]]

for num in s:
    subsets += [curr + [num] for curr in subsets]

print(subsets)

#___________________________________________________________________________________________________________________________________#

# Problem23: Implement a function that rotates a matrix 90 degrees clockwise.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = [list(row) for row in zip(*matrix[::-1])]

print("Rotated matrix:")
for row in rotated_matrix:
    print(row)



#___________________________________________________________________________________________________________________________________#

# Problem24: Write a Python program to convert a Roman numeral to an integer.

roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
roman = "MCMXCIV"

result = 0
prev_value = 0
for char in reversed(roman):
    value = roman_to_int[char]
    if value < prev_value:
        result -= value
    else:
        result += value
    prev_value = value

print("Integer value of", roman, ":", result)


#___________________________________________________________________________________________________________________________________#

# Problem25: Implement a program that evaluates a postfix expression using a stack.

expression = "231*+9-"

stack = []

for char in expression:
    if char.isdigit():
        stack.append(int(char))  # Push operand to stack
    else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a // b)

print(stack.pop())
