"""
Problem Statement:
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".

Intuition:
This problem tests your understanding of the modular operator ($\bmod$) and control flow. The key insight is that you need to handle the most specific condition (divisible by both 3 AND 5) correctly. Instead of checking divisibility by 15 first, you can build the output string incrementally — append "Fizz" if $n \bmod 3 = 0$, then append "Buzz" if $n \bmod 5 = 0$. This naturally produces "FizzBuzz" for multiples of both.

Approach:
1. Loop through numbers 1 to 100.
2. For each number, initialize an empty string.
3. If $n \bmod 3 = 0$, append "Fizz" to the string.
4. If $n \bmod 5 = 0$, append "Buzz" to the string.
5. If the string is still empty (not divisible by 3 or 5), print the number itself.
6. Otherwise, print the constructed string.

Time Complexity:
$O(N)$ where $N$ is the range of numbers (100 in this case)

Space Complexity:
$O(1)$ — only a single output string variable is used

Common Mistakes:
- Checking divisibility by 3 before checking for both 3 and 5, which causes "FizzBuzz" cases to print only "Fizz"
- Using `elif` instead of separate `if` statements when building the string incrementally
- Forgetting that $0 \bmod 3 = 0$ is true, so starting from 0 instead of 1 gives an extra empty output

Code Explanation:
- `def fizzbuzz()`: Defines a function with no parameters.
- `for i in range(1, 101)`: Loops from 1 to 100 inclusive. `range(1, 101)` excludes 101.
- `output = ""`: Starts with an empty string each iteration; we'll build into it.
- `if i % 3 == 0: output += "Fizz"`: `%` is the modulo operator; remainder is 0 when divisible.
- `if i % 5 == 0: output += "Buzz"`: Uses a separate `if` (not `elif`) so both branches can fire on multiples of 15.
- `print(output or i)`: Python's `or` returns the first truthy value; if `output` is `""` (falsy), it prints `i` instead.

Final Thoughts:
FizzBuzz is a classic interview warm-up that tests basic control flow and the modular operator. The string-building approach is more elegant than checking for 15 first, and it scales better if more conditions are added (e.g., "Jazz" for multiples of 7).
"""

# Question: Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        
        # If output is empty (i.e. not divisible by 3 or 5), print the number
        print(output or i)

fizzbuzz()