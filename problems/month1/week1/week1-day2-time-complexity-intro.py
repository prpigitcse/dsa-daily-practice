"""
Problem Statement:
Write a function that calculates the sum of all natural numbers from 1 to N. Implement two approaches: a loop-based $O(N)$ solution and a formula-based $O(1)$ solution using the Gauss identity $\frac{N(N+1)}{2}$.

Intuition:
This problem introduces time complexity by showing two algorithms that produce identical results but with vastly different performance. The brute-force loop visits every number in $O(N)$ time. The Gauss formula $\sum_{i=1}^{N} i = \frac{N(N+1)}{2}$ computes the answer in $O(1)$ — instantly regardless of $N$.

Approach:
1. **Approach A (Loop):** Initialize `total = 0`. Loop from 1 to N, adding each number. Return `total`.
2. **Approach B (Math):** Use the formula $\frac{N(N+1)}{2}$ with integer division. This is a single operation.
3. **Compare:** For $N = 1{,}000{,}000$, Approach A performs 1 million additions. Approach B performs 1 multiplication and 1 division.

Time Complexity:
$O(N)$ for the loop approach; $O(1)$ for the mathematical formula

Space Complexity:
$O(1)$ for both approaches — only a single variable is used

Common Mistakes:
- Using floating-point division `/` instead of integer division `//` in the formula, leading to precision issues for large $N$
- Off-by-one error: using `range(1, n)` instead of `range(1, n + 1)` in the loop
- Not recognizing that the formula can overflow in languages with fixed integer sizes (not an issue in Python)

Code Explanation:
**Approach A — `sum_natural_numbers_loop(n)`:**
- `total = 0`: Accumulator variable initialized to zero.
- `for i in range(1, n + 1)`: Iterates from 1 to n inclusive; `n + 1` ensures n is included.
- `total += i`: Adds the current number to the running sum on each iteration.
- `return total`: Returns the accumulated sum after all iterations.

**Approach B — `sum_natural_numbers(n)`:**
- `return n * (n + 1) // 2`: A single expression applying the Gauss formula. `//` is integer division, avoiding floating-point results. No loop needed.

Final Thoughts:
This is your first lesson in algorithmic thinking: the same problem can be solved in dramatically different ways. Always ask "Is there a mathematical shortcut?" before writing a loop. Understanding $O(N)$ vs $O(1)$ here sets the stage for everything that follows.
"""

# Question: Write a function that calculates the sum of all natural numbers from 1 to N. (e.g., if N=5, output 1+2+3+4+5 = 15).

# Approach A
def sum_natural_numbers_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Approach B
def sum_natural_numbers(n):
    return n * (n + 1) // 2

print(sum_natural_numbers_loop(5))
print(sum_natural_numbers(5))