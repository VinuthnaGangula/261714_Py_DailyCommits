# To split a string with spaces and join them with '-'.

if __name__ == "__main__":
    line = input("Enter the string: ")
    result = "-".join(line.split(" "))
    print(result)


# Sample Input
# Enter the string: This is my PC
# Output
# This-is-my-PC
