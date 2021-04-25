# Using try, except for exception handling

if __name__ == "__main__":
    try:
        a, b = input("Enter a and b: ").split()
        print(int(a) // int(b))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)

# Sample Input
# Enter a and b: 1 0
# Output
# Error Code: integer division or modulo by zero
