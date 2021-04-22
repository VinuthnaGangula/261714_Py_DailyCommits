# To find second smallest element in a list

n = int(input("Enter no. of scores: "))
list_ = list(map(int, input("Enter n scores separated by a space: ").split()))

smallest = min(list_)
list_ = list(filter(lambda x: x != smallest, list_))
second_smallest = min(list_)
print("Second smallest element in the list: " + str(second_smallest))

# Sample Input
# Enter no. of scores: 4
# Enter n scores separated by a space: 1 3 7 2

# Output
# Second smallest element in the list: 2
