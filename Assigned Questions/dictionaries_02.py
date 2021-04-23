# To convert a list into nested dictionary of keys.

list_ = list(input("Enter values of the list: ").split())

dict_ = {}
dict_temp = dict_
for i in list_:
    dict_[i] = {}
    dict_ = dict_[i]
print(dict_temp)
