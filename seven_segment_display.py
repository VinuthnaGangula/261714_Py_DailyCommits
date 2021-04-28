# To display numbers in as a number in seven segment display

list_ = list(map(int, input()))

num_list_1 = ["###", "#", "###", "###", "# #", "###", "###", "###", "###", "###"]
num_list_2 = ["# #", "#", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"]
num_list_3 = ["# #", "#", "###", "###", "###", "###", "###", "  #", "###", "###"]
num_list_4 = ["# #", "#", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"]
num_list_5 = ["###", "#", "###", "###", "  #", "###", "###", "  #", "###", "###"]

for i in list_:
    print(num_list_1[i], end=" ")
print()
for i in list_:
    print(num_list_2[i], end=" ")
print()
for i in list_:
    print(num_list_3[i], end=" ")
print()
for i in list_:
    print(num_list_4[i], end=" ")
print()
for i in list_:
    print(num_list_5[i], end=" ")
