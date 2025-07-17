"""# Docstring Generator Example

This example demonstrates how to use a language model to generate Python docstrings for functions using the LangChain framework and Gradio for the user interface."

```python sample codes to test the docstring generator


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def is_prime(n):
    if n <= 1:
        return False    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 

    return True 
  
"""        