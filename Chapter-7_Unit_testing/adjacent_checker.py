from divisor_utils import count_total_divisors

def count_adjacent_numbers_with_equal_divisors(limit):
    """
    Counts how many times consecutive numbers (x and x+1) from 2 to (limit - 1)
    have the same number of divisors.
    """
    matching_pair_count = 0
    for current in range(2, limit):
        if count_total_divisors(current) == count_total_divisors(current + 1):
            matching_pair_count += 1
    return matching_pair_count
