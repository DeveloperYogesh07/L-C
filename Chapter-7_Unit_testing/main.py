from adjacent_checker import count_adjacent_numbers_with_equal_divisors

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
