def find_factors(n: int) -> None:
    """Print all factors of a given positive integer."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")


if __name__ == "__main__":
    # Get user input
    n = int(input("Enter a positive integer: "))

    # Ensure input is positive
    if n > 0:
        find_factors(n)
    else:
        print("Please enter a positive integer.")
