# To print 1 to n numbers in the same line using print().
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    i = 1
    while i <= n:
        print(i, end='')
        i += 1

# Sample Input
# Enter a number: 5
# Output
# 12345
