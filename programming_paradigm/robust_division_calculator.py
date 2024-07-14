def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    # Example usage
    print(safe_divide(10, 5))  # Expected Output: The result of the division is 2.00
    print(safe_divide(10, 0))  # Expected Output: Error: Cannot divide by zero.
    print(safe_divide("ten", 5))  # Expected Output: Error: Please enter numeric values only.
