test_samples = [
    {
        "code": "def is_even(num):\n    return num % 2 == 0",
        "expected": "Checks if a number is even and returns True or False."
    },
    {
        "code": "def square(n):\n    return n * n",
        "expected": "Returns the square of the input number."
    },
    {
        "code": "def greet(name):\n    return f'Hello, {name}!'",
        "expected": "Returns a greeting message with the given name."
    },
    {
        "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
        "expected": "Calculates the factorial of a non-negative integer recursively."
    },
    {
        "code": "def reverse_string(s):\n    return s[::-1]",
        "expected": "Returns the reverse of the given string."
    },
    {
        "code": "def max_of_two(a, b):\n    return a if a > b else b",
        "expected": "Returns the maximum of two numbers."
    },
    {
        "code": "def is_palindrome(word):\n    return word == word[::-1]",
        "expected": "Checks if a word is a palindrome."
    },
    {
        "code": "def sum_list(numbers):\n    return sum(numbers)",
        "expected": "Returns the sum of all elements in the list."
    },
    {
        "code": "def get_first_element(lst):\n    return lst[0]",
        "expected": "Returns the first element of the list."
    },
    {
        "code": "def count_vowels(s):\n    return sum(1 for c in s if c.lower() in 'aeiou')",
        "expected": "Counts and returns the number of vowels in the given string."
    },
    {
        "code": "def merge_dicts(d1, d2):\n    return {**d1, **d2}",
        "expected": "Merges two dictionaries and returns the result."
    },
    {
        "code": "def is_positive(n):\n    return n > 0",
        "expected": "Checks if a number is positive."
    },
    {
        "code": "def to_uppercase(s):\n    return s.upper()",
        "expected": "Converts the string to uppercase."
    },
    {
        "code": "def average(numbers):\n    return sum(numbers) / len(numbers)",
        "expected": "Calculates the average of a list of numbers."
    },
    {
        "code": "def get_last_char(s):\n    return s[-1]",
        "expected": "Returns the last character of a string."
    }
]
