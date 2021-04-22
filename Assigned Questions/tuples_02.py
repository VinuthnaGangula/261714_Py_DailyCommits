# To convert a list of tuples into Dictionary.

n = int(input("Enter no. of tuples: "))
list_ = []
for i in range(1, n+1):
    tuple_ = tuple(input("Enter tuple: ").split())
    list_.append(tuple_)
print("Before conversion: ")
print(list_)
dict_ = {}
for i in list_:
    dict_[i[0]] = i[1]
print("After conversion: ")
print(dict_)

# Sample Input

# Enter no. of tuples: 2
# Enter tuple: A 1
# Enter tuple: B 2

# Output

# Before conversion:
# [('A', '1'), ('B', '2')]
# After conversion:
# {'A': '1', 'B': '2'}
