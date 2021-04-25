# To find polar coordinates of a given complex number

import cmath

if __name__ == "__main__":
    s = complex(input("Enter complex number: "))
    r = abs(s)
    ph = cmath.phase(s)
    print("Polar coordinates (r,ph): (" + str(r) + ", " + str(ph) + ")")

# Sample Input
# Enter complex number: 1+2j
# Output
# Polar coordinates (r,ph): (2.23606797749979, 1.1071487177940904)
