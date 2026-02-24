"""
Pattern:
Recursion

Problem Statement:
Write a function `factorial(n)` that returns $n!$ (n factorial). $n! = n \times (n-1) \times (n-2) \times \cdots \times 1$. By definition, $0! = 1$. Input: 5 → Output: 120. You must use recursion — no for or while loops allowed.

Intuition:
Recursion breaks a problem into smaller versions of itself. Factorial has a natural recursive definition: $n! = n \times (n-1)!$. The base case is $0! = 1$. Each recursive call reduces $n$ by 1, and results multiply on the way back up the call stack.

Approach:
1. Base case: if $n = 0$, return 1.
2. Recursive case: return $n \times \text{factorial}(n - 1)$.
3. Validate: raise an error for negative numbers (factorial is undefined for $n < 0$).

Time Complexity:
$O(N)$ — we make $N$ recursive calls, each doing $O(1)$ work

Space Complexity:
$O(N)$ — the call stack holds $N$ frames at its deepest point

Common Mistakes:
- Forgetting the base case ($n = 0$), causing infinite recursion and a stack overflow
- Using $n = 1$ as the base case, which makes `factorial(0)` recurse infinitely
- Not handling negative inputs (factorial undefined for $n < 0$)
- Confusing recursion depth with time complexity — they are both $O(N)$ here

Code Explanation:
- `def factorial(n)`: The function calls itself, so it must be named and defined before the recursive call.
- `if n < 0: raise ValueError(...)`: Guard against invalid input; factorial is not defined for negative numbers.
- `if n == 0: return 1`: **Base case**: stops the recursion. Without this, the function would call itself forever.
- `return n * factorial(n-1)`: **Recursive case**: multiplies `n` by the result of the same function called with `n-1`. The multiplication is deferred until the stack unwinds (Python evaluates `factorial(n-1)` first).
- For `factorial(3)`, the call stack looks like: `3 * factorial(2)` → `3 * 2 * factorial(1)` → `3 * 2 * 1 * factorial(0)` → `3 * 2 * 1 * 1 = 6`.

Final Thoughts:
Factorial is the "Hello World" of recursion. It teaches the two essential components: a base case that stops recursion, and a recursive case that reduces the problem. Watch out for Python's default recursion limit of 1000 for large $N$.
"""

# The Problem: Calculate Factorial
# Write a function factorial(n) that returns n!
# n! = n * (n-1) * (n-2) ... * 1
# 0! = 1 (Mathematical definition)
# Input: 5 Output: 120 (5 * 4 * 3 * 2 * 1)
# Input: 0 Output: 1
# Constraint: You must use Recursion. Do not use a for or while loop.

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))