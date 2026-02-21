"""
Problem Statement:
An Armstrong number (also called a Narcissistic number) of N digits is a number where the sum of each digit raised to the power of N equals the number itself. For example, 153 is Armstrong because 1^3 + 5^3 + 3^3 = 153. Check if a given number is an Armstrong number.

Intuition:
This is another application of the digit extraction pattern. First, count how many digits the number has (this determines the power N). Then extract each digit, raise it to the Nth power, and sum them up. If the sum equals the original number, it is an Armstrong number. The key insight is making the power dynamic based on digit count, not hardcoded to 3.

Approach:
1. Count the number of digits using a helper function (repeatedly divide by 10 and count).
2. Store the original number.
3. Extract each digit using % 10, raise it to the power of num_digits, and add to a running sum.
4. Remove the digit with // 10. Repeat until the number is 0.
5. Compare the sum with the original — if equal, it is an Armstrong number.

Time Complexity:
O(log N) where N is the value of the number — we process each digit once (twice with digit counting)

Space Complexity:
O(1) — only a few integer variables

Common Mistakes:
- Hardcoding the power to 3, which only works for 3-digit numbers (fails for 1634, a 4-digit Armstrong number: 1^4 + 6^4 + 3^4 + 4^4 = 1634)
- Forgetting to preserve the original number before extracting digits
- Not handling 0 correctly as an edge case (0 is technically an Armstrong number: 0^1 = 0)
- Negative numbers should return False

Final Thoughts:
Armstrong number checking reinforces the digit extraction loop and adds the concept of dynamic power based on digit count. The helper function for counting digits is a good exercise in code modularity. Some known Armstrong numbers: 0, 1, 153, 370, 371, 407, 1634, 8208, 9474.
"""

# Check for Armstrong Number
# An Armstrong number (for the purpose of this basic exercise, we'll focus on 3-digit numbers) is a number that equals the sum of its digits each raised to the power of 3.Input: 153Calculation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# Output: True Input: 123
# Calculation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
# Output: FalseGeneral Rule (for extra credit):Strictly speaking, an Armstrong number of N digits is the sum of its digits raised to the power of N. (e.g., for 1634, N=4: 1^4 + 6^4 + 3^4 + 4^4 = 1634).Goal: Write a function that checks if a number is an Armstrong number. You can stick to the power of 3 for now, or make it dynamic based on the number of digits (more robust).

def number_of_digits(num):
    if num == 0:
        return 1
    digits = 0
    while num > 0:
        num //= 10
        digits += 1
    
    return digits

def is_armstrong(num):
    if num < 0:
        return False
    num_digits = number_of_digits(num)
    sum_of_power = 0
    original = num

    while num > 0:
        digit = num % 10
        sum_of_power += digit ** num_digits
        num //= 10
    
    return sum_of_power == original

print(is_armstrong(153))