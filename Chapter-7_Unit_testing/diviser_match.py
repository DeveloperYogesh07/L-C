def count_total_divisors(number):
    """Returns the total number of divisors of a given number."""
    divisor_count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisor_count += 2 if i != number // i else 1
    return divisor_count


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


def main():
    test_cases = int(input("Enter number of test cases: "))
    results = []
    for _ in range(test_cases):
        limit = int(input("Enter upper limit n: "))
        result = count_adjacent_numbers_with_equal_divisors(limit)
        results.append(result)

    print("\nResults:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
