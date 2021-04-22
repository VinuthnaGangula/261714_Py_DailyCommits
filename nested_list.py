# To print names of the students with second lowest score alphabetically, given grades of students
if __name__ == "__main__":
    list_ = []
    for i in range(int(input("Enter n: "))):
        name = input("Enter name " + str(i+1) + ": ")
        score = float(input("Enter score " + str(i+1) + ": "))
        temp = [name, score]
        list_.append(temp)
    min_score = list_[0][1]
    for i in list_:
        if i[1] < min_score:
            min_score = i[1]

    list_ = list(filter(lambda x: x[1] != min_score, list_))

    min_score = list_[0][1]
    for i in list_:
        if i[1] < min_score:
            min_score = i[1]

    list_ = list(filter(lambda x: x[1] == min_score, list_))
    list_.sort()
    for i in list_:
        print(i[0])

# Sample Input

# Enter n: 5
# Enter name 1: Harry
# Enter score 1: 37.21
# Enter name 2: Berry
# Enter score 2: 37.21
# Enter name 3: Tina
# Enter score 3: 37.2
# Enter name 4: Akriti
# Enter score 4: 41
# Enter name 5: Harsh
# Enter score 5: 39

# Output

# Berry
# Harry

