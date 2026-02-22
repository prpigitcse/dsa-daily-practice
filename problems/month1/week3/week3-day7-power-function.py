"""
Problem Statement:
Write a recursive function `power(x, n)` that calculates $x^n$. Input: $x = 2, n = 10$ → Output: 1024. You must use recursion and must not use the `**` operator. Naive multiplication is $O(N)$ — achieve $O(\log N)$.

Intuition:
**Exponentiation by squaring**: $x^n = (x^{n/2})^2$ when $n$ is even. This halves the problem at each step, giving $O(\log N)$. For odd $n$: $x^n = x \cdot (x^{\lfloor n/2 \rfloor})^2$. This mirrors the binary search halving principle, applied to computation.

Approach:
1. Base case: if $n = 0$, return 1 (by definition $x^0 = 1$).
2. Recursively compute $\text{half} = \text{power}(\text{base}, \lfloor n/2 \rfloor)$.
3. If $n$ is even: return $\text{half}^2$.
4. If $n$ is odd: return $\text{base} \times \text{half}^2$.

Time Complexity:
$O(\log N)$ where $N$ is the exponent — we halve the exponent with each recursive call

Space Complexity:
$O(\log N)$ for the recursion stack

Common Mistakes:
- Using a simple loop ($x \times x \times \cdots$, $n$ times) — $O(N)$, too slow for $n = 10^6$
- Computing `power(base, exp // 2)` **twice** instead of storing the result — turns $O(\log N)$ into $O(N)$
- Not handling $n = 0$ as the base case
- Forgetting the odd exponent case: $x^5 = x \cdot (x^2)^2$, not just $(x^2)^2$

Code Explanation:
- `def power(base, exp)`: Takes the base $x$ and the exponent $n$.
- `if exp < 0: raise ValueError(...)`: Guard against negative exponents.
- `if exp == 0: return 1`: **Base case**: anything to the power 0 is 1.
- `half = power(base, exp // 2)`: Recursively compute $x^{n/2}$. `exp // 2` uses integer division (floor). **Crucially**, this result is stored in `half` and reused — not called twice.
- `if exp % 2 == 0: return half * half`: Even exponent: $x^n = (x^{n/2})^2 = \text{half} \times \text{half}$.
- `else: return base * half * half`: Odd exponent: $x^n = x \cdot (x^{\lfloor n/2 \rfloor})^2 = \text{base} \times \text{half} \times \text{half}$.

Final Thoughts:
Fast exponentiation (binary exponentiation) reduces $10^6$ multiplications to about 20. It underpins modular exponentiation in RSA cryptography, matrix exponentiation for Fibonacci, and competitive programming. "Compute half, then combine" is the essence of divide and conquer.
"""

# The Problem: Calculate x^n
# Write a recursive function power(x, n) that calculates x raised to the power of n.
# Input: x = 2, n = 10 Output: 1024
# Input: x = 3, n = 3 Output: 27
# Constraint: You must use Recursion. You cannot use the built-in ** operator for the whole problem.

def power(base, exp):
    if exp < 0:
        raise ValueError("Exponent must be >= 0")

    if exp == 0:
        return 1

    # Recursive call
    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half

print(power(2, 10))   # 1024
