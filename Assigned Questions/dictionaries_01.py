# Merging two dictionaries

# dict_1 = {'A': 1, 'B': 2, 'C': 3}
# dict_2 = {'X': -3, 'Y': -2, 'Z': -1}
dict_1 = {}
dict_2 = {}

n = int(input("Enter no. of elements in dict_1: "))
for i in range(1, n+1):
    k = input("Enter key " + str(i) + ": ")
    v = input("Enter value " + str(i) + ": ")
    dict_1[k] = v

n = int(input("Enter no. of elements in dict_2: "))
for i in range(1, n+1):
    k = input("Enter key " + str(i) + ": ")
    v = input("Enter value " + str(i) + ": ")
    dict_2[k] = v
print("Dictionaries before merging: ")
print(dict_1, dict_2)
for k, v in dict_2.items():
    dict_1[k] = v
print("Dictionaries after merging: ")
print(dict_1, dict_2)
