"""
This python module will have reusable numerical functions
   is_even
   is_prime
"""
import heartrate
heartrate.trace(browser=True)


def is_even(number: int):
    """Finds if the number is even or odd

    Args:
      number: Number passed

    Returns:
      True if even, False otherwise

    Usage:
       is_even(6)
       Return True
    """
    if number <= 0:
        return False
    result = number%2 == 0
    return result


for index in range(10,25):
    if is_even(index):
        print(index, end=" ")