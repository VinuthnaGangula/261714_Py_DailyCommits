# Change the string to Title case.

if __name__ == "__main__":
    s = input("Enter the string: ")
    list_ = s.split(" ")
    result = " ".join(i.capitalize() for i in list_)
    print(result)

# Sample Input
# Enter the string: larsen and toubro
# Output
# Larsen And Toubro
