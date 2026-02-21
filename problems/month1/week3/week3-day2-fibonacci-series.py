"""
Problem Statement:
Write a recursive function fib(n) that returns the n-th Fibonacci number. The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... where F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. Input: 6 → Output: 8. Input: 7 → Output: 13.

Intuition:
Fibonacci has a natural recursive structure: each value depends on the two before it. The naive recursive solution directly mirrors the mathematical definition. However, this creates a binary tree of calls where many subproblems are computed repeatedly (e.g., fib(3) is computed multiple times when calculating fib(6)). This is a classic example of overlapping subproblems.

Approach:
1. Base cases: if n == 0, return 0. If n == 1, return 1.
2. Recursive case: return fib(n - 1) + fib(n - 2).
3. Each call branches into two sub-calls, creating a binary recursion tree.

Time Complexity:
O(2^N) — exponential, because each call generates two new calls. This is very slow for n > 30

Space Complexity:
O(N) — the maximum depth of the recursion tree is N

Common Mistakes:
- Not having two base cases (both n == 0 and n == 1 are needed)
- Assuming this approach is efficient — it is O(2^N) and should be optimized with memoization or dynamic programming for real use
- Off-by-one errors in the sequence indexing (is fib(6) = 8 or 13? Depends on 0-indexing vs 1-indexing)
- Confusing Fibonacci with factorial — they have similar recursive structures but different operations

Final Thoughts:
Naive recursive Fibonacci is intentionally inefficient. The purpose is to understand how recursion can lead to redundant work. This sets the stage for memoization and dynamic programming, which reduce the complexity to O(N). The Fibonacci sequence appears in nature, computer science, and mathematics — mastering it recursively first is essential before optimizing.
"""

# The Problem: The N-th Fibonacci Number
# The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Write a function fib(n) that returns the n-th number in the sequence.
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
# Input: 6 -> Output: 8
# Input: 7 -> Output: 13
# Constraint:You must use Recursion. Do not use a loop.

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))