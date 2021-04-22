# Program to find repeated items of a tuple.
tuple_ = (input("Enter values of tuple: ").split())
set_ = set(tuple_)
list_ = list(tuple_)
for i in set_:
    list_.remove(i)
print("Repeated items in the tuple are: " + str(tuple(list_)))

# Sample Input

# Enter values of tuple: 1 2 3 4 4 6 2 1

# Output

# Repeated items in the tuple are: ('4', '2', '1')
