import math

def solve():
    # Read the input values Y and W
    Y, W = map(int, input().split())
    
    # Find the maximum of Yakko's and Wakko's rolls
    M = max(Y, W)
    
    # Number of favorable outcomes for Dot
    favorable_outcomes = 7 - M  # Dot wins if she rolls M, M+1, ..., 6
    
    # Total possible outcomes for Dot (6 sides of the die)
    total_outcomes = 6
    
    # Simplify the fraction
    gcd_value = math.gcd(favorable_outcomes, total_outcomes)
    
    # Output the result in the form "A/B"
    print(f"{favorable_outcomes // gcd_value}/{total_outcomes // gcd_value}")

