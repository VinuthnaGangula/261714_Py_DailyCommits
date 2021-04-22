# To find the maximum and the minimum value in a set.

n = int(input("Enter no. of elements in the set: "))
set_ = set()
for i in range(1, n+1):
    set_.add(input("Enter element " + str(i) + ": "))
print("Maximum value in the set: " + str(max(set_)))
print("Minimum value in the set: " + str(min(set_)))

# Sample Input

# Enter no. of elements in the set: 4
# Enter element 1: 1
# Enter element 2: 1
# Enter element 3: 3
# Enter element 4: 5

# Output

# Maximum value in the set: 5
# Minimum value in the set: 1
