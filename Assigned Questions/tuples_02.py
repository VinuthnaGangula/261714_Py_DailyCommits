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
