def convert_cel_to_far(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    # Convert Fahrenheit to Celsius
    f_temp = float(input("Enter a temperature in degrees F: "))
    c_temp = convert_far_to_cel(f_temp)
    print(f"{f_temp} degrees F = {c_temp:.2f} degrees C")

    # Convert Celsius to Fahrenheit
    c_temp = float(input("\nEnter a temperature in degrees C: "))
    f_temp = convert_cel_to_far(c_temp)
    print(f"{c_temp} degrees C = {f_temp:.2f} degrees F")