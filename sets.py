# Using sets to find average of distinct heights of plant samples

if __name__ == "__main__":
    n = int(input("Enter no. of plant samples: "))
    arr = set(map(int, input("Enter heights of plants: ").split()))
    avg = sum(arr)/len(arr)
    print(round(avg, 3))

# Sample Input
# Enter no. of plant samples: 10
# Enter heights of plants: 161 182 161 154 176 170 167 171 170 174
# Output
# 169.375
