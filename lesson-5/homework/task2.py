def invest(amount: float, rate: float, years: int) -> None:
    """Calculate and display the growth of an investment over time."""
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"Year {year}: ${amount:.2f}")


if __name__ == "__main__":
    # Get user input
    amount = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))

    # Call invest function
    invest(amount, rate, years)
