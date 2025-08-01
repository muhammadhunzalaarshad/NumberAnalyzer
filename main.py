from functools import reduce
from typing import List

def find_primes(numbers: List[int]) -> List[int]:
    """
    Find prime numbers in a given list of integers.
    Args:
        numbers: List of integers to check for primality.
    Returns:
        List of prime numbers found in the list.
    """
    prime_numbers = []
    for number in numbers:
        if number > 1:
            for divisor in range(2, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers

def count_factors(number: int) -> int:
    """
   Calculate the total number of distinct factors for a given integer.

    Args:
        number: Integer to find factors for.

    Returns:
        Count of distinct factors of the number.
    """
    factors = []
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            factors.append(divisor)
            if number // divisor  != divisor:
                factors.append(number // divisor)            
    return len(factors)

def lcm_func(number_1: int, number_2: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers using the Euclidean algorithm.

    Args:
        number_1: First integer.
        number_2: Second integer.

    Returns:
        LCM of the two numbers.
    """
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    return (number_1 * number_2) // gcd(number_1, number_2)

def main() -> None:

    try:
        with open("numbers.txt", "r") as file:         
            content = file.read().splitlines()
            numbers = [int(num.strip()) for num in content if num.strip()]

            if not numbers:
                raise ValueError("File is empty or contains no valid numbers")
            if any(num <= 0 for num in numbers):
                raise ValueError("File contains negative or zero numbers")
            
            print(f"Numbers in file: {numbers}")
            print(f"Prime numbers: {find_primes(numbers)}")
            print("Factors count")
            for num in numbers:
                print(f"- {num} has {count_factors(num)}")
            print(f"LCM of all numbers: {reduce(lcm_func, numbers)}")

    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
                print("Error: numbers.txt file not found")

if __name__ == "__main__":
    main()


