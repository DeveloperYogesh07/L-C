def count_total_divisors(number):
    """Returns the total number of divisors of a given number."""
    divisor_count = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor_count += 2 if i != number // i else 1
    return divisor_count
