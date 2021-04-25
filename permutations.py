# To use itertools.permutations()

from itertools import permutations

if __name__ == "__main__":
    s, n = input("Enter string and size: ").split()
    res = list(permutations(s, int(n)))
    res = list(map(lambda x: "".join(x), res))
    res.sort()
    for i in res:
        print(i)

# Sample Input
# Enter string and size: HACK 2
# Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
