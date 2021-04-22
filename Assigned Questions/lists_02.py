# To change position of every nth value with (n+1)th in a list

n = int(input("Enter no. of elements in list: "))
list_ = list(input("Enter elements of the list - space separated: ").split())
print("Before: " + str(list_))

first = list_[0]
for i in range(n-1):
    list_[i] = list_[(i + 1)]
list_[n-1] = first
print("After: " + str(list_))

# Sample Input
# Enter no. of elements in list: 4
# Enter elements of the list - space separated: 1 2 3 4

# Output
# Before: ['1', '2', '3', '4']
# After: ['2', '3', '4', '1']
