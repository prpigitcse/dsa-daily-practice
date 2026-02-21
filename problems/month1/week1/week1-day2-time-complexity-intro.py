"""
Problem Statement:
Write a function that calculates the sum of all natural numbers from 1 to N. Implement two approaches: a loop-based O(N) solution and a formula-based O(1) solution using the mathematical identity N*(N+1)/2.

Intuition:
This problem introduces the concept of time complexity by showing two different algorithms that produce identical results but with vastly different performance characteristics. The brute-force loop visits every number, while the math formula computes the answer instantly regardless of N. This demonstrates why algorithm optimization matters.

Approach:
1. Approach A (Loop): Initialize a total variable to 0. Loop from 1 to N, adding each number to total. Return total.
2. Approach B (Math): Use the Gauss summation formula: N * (N + 1) // 2. This gives the result in a single operation.
3. Compare: For N = 1,000,000, Approach A performs 1 million additions. Approach B performs 1 multiplication and 1 division.

Time Complexity:
O(N) for the loop approach, O(1) for the mathematical formula

Space Complexity:
O(1) for both approaches — only a single variable is used

Common Mistakes:
- Using floating-point division (/) instead of integer division (//) in the formula, leading to precision issues for large N
- Off-by-one error: using range(1, n) instead of range(1, n + 1) in the loop
- Not recognizing that the formula can overflow in languages with fixed integer sizes (not an issue in Python)

Final Thoughts:
This is your first lesson in algorithmic thinking: the same problem can be solved in dramatically different ways. Always ask "Is there a mathematical shortcut?" before writing a loop. Time complexity is the foundation of DSA — understanding O(N) vs O(1) here sets the stage for everything that follows.
"""

# Question: Write a function that calculates the sum of all natural numbers from 1 to N. (e.g., if N=5, output 1+2+3+4+5 = 15).

# Explanation & Logic:There are two ways to solve this.
# Approach A (Loop): You loop from 1 to N adding to a variable. This takes O(N) time (Linear Time).

# Approach B (Math): You use the summation formula {N(N+1)}/{2}. This takes O(1) time (Constant Time).Goal: Implement both to see how algorithms can be optimized using math instead of brute force.

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