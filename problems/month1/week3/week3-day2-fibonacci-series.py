"""
Problem Statement:
Write a recursive function `fib(n)` that returns the $n$-th Fibonacci number. The sequence is: $F(0) = 0,\; F(1) = 1,\; F(n) = F(n-1) + F(n-2)$ for $n > 1$. Input: 6 → Output: 8. Input: 7 → Output: 13.

Intuition:
Fibonacci has a natural recursive structure: each value depends on the two preceding it. The naive recursive solution mirrors the mathematical definition, but creates a binary tree of calls with many **overlapping subproblems** (e.g., $F(3)$ is computed multiple times for $F(6)$).

Approach:
1. Base cases: if $n = 0$, return 0. If $n = 1$, return 1.
2. Recursive case: return $\text{fib}(n-1) + \text{fib}(n-2)$.
3. Each call branches into two sub-calls, creating a binary recursion tree.

Time Complexity:
$O(2^N)$ — exponential, because each call generates two new calls. Very slow for $N > 30$.

Space Complexity:
$O(N)$ — the maximum depth of the recursion tree is $N$

Common Mistakes:
- Not having two base cases (both $n = 0$ and $n = 1$ are needed)
- Assuming this approach is efficient — it is $O(2^N)$ and should be memoized for real use
- Off-by-one errors in sequence indexing ($F(6) = 8$ with 0-indexing)
- Confusing Fibonacci with factorial — similar structure, different operations

Code Explanation:
- `def fib(n)`: Recursive function; must be defined with the same name for the self-call to work.
- `if n == 0 or n == 1: return n`: **Two base cases** in one line. `return n` works because `fib(0) = 0` and `fib(1) = 1` (the value equals the index).
- `return fib(n-1) + fib(n-2)`: **Recursive case**: the $n$-th term is the sum of the previous two. This spawns two sub-calls at each level.
- For `fib(4)`: `fib(3) + fib(2)` → `(fib(2) + fib(1)) + (fib(1) + fib(0))` → `((fib(1) + fib(0)) + 1) + (1 + 0)` → `((1 + 0) + 1) + 1 = 3$. Notice `fib(1)` and `fib(0)` are each computed multiple times — this redundancy is why it's $O(2^N)$.

Final Thoughts:
Naive recursive Fibonacci is intentionally slow. Its purpose is to show how recursion can cause redundant work. This sets the stage for memoization, which reduces complexity to $O(N)$, and dynamic programming.
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
# Constraint: You must use Recursion. Do not use a loop.

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))