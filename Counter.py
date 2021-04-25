# To use collections.Counter()

from collections import Counter

if __name__ == "__main__":
    n = int(input("Enter no. of shoe sizes: "))
    shoe_sizes = list(map(int, input("Enter space separates shoe sizes: ").split()))

    dict_ = dict(Counter(shoe_sizes))
    total = 0

    nc = int(input("Enter no. of customers: "))
    for i in range(1, nc+1):
        size, price = map(int, input("Enter size and price of customer " + str(i) + ": ").split())
        if (size in dict_.keys()) and dict_[size] > 0:
            dict_[size] -= 1
            total += price

    print(total)

# Sample Input
# Enter no. of shoe sizes: 10
# Enter space separates shoe sizes: 2 3 4 5 6 8 7 6 5 18
# Enter no. of customers: 6
# Enter size and price of customer 1: 6 55
# Enter size and price of customer 2: 6 45
# Enter size and price of customer 3: 6 55
# Enter size and price of customer 4: 4 40
# Enter size and price of customer 5: 18 60
# Enter size and price of customer 6: 10 50
# Output
# 200
