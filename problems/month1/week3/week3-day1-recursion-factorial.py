"""
Problem Statement:
Write a function factorial(n) that returns n! (n factorial). n! = n × (n-1) × (n-2) × ... × 1. By definition, 0! = 1. Input: 5 → Output: 120 (5 × 4 × 3 × 2 × 1). Input: 0 → Output: 1. You must use recursion — no for or while loops allowed.

Intuition:
Recursion is about breaking a problem into smaller versions of itself. The factorial has a natural recursive definition: n! = n × (n-1)!. The base case is 0! = 1. Each recursive call reduces the problem by 1, and the results multiply on the way back up the call stack. This is your introduction to "thinking recursively."

Approach:
1. Base case: if n == 0, return 1.
2. Recursive case: return n * factorial(n - 1).
3. Validate input: raise an error for negative numbers (factorial is undefined for negatives).

Time Complexity:
O(N) — we make N recursive calls, each doing O(1) work

Space Complexity:
O(N) — the call stack holds N frames at its deepest point

Common Mistakes:
- Forgetting the base case (n == 0), causing infinite recursion and a stack overflow
- Using n == 1 as the base case, which makes factorial(0) recurse infinitely
- Not handling negative inputs (factorial is undefined for negative numbers)
- Confusing recursion depth with time complexity — they are both O(N) here

Final Thoughts:
Factorial is the "Hello World" of recursion. It teaches the two essential components of any recursive solution: a base case that stops the recursion, and a recursive case that reduces the problem size. Every recursive problem you encounter will follow this same structure. Watch out for Python's default recursion limit of 1000 for large N.
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