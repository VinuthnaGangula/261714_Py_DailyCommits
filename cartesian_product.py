# To print cartesian product of two lists using itertools.product()
from itertools import product

if __name__ == "__main__":
    a = list(map(int, input("Enter space separated values of list 1: ").split()))
    b = list(map(int, input("Enter space separated values of list 2: ").split()))

    res = list(product(a, b))
    for i in res:
        print(i, end=" ")

# Sample Input
# Enter space separated values of list 1: 1 2
# Enter space separated values of list 2: 3 4
# Output
# (1, 3) (1, 4) (2, 3) (2, 4)
