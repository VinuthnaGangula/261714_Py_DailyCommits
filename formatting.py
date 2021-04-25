# print 1 to n numbers in different number format using string formatting.

def print_formatted(n):
    w = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print(f"{i: {w}d} {i: {w}o} {i: {w}X} {i: {w}b}")


if __name__ == "__main__":
    number = int(input("Enter the number: "))
    print_formatted(number)

# Sample Input
# Enter the number: 2
# Output
# 1  1  1  1
#  2  2  2  10
